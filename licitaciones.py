import requests
import logging
import re

class LicitacionesExtractor:
    def __init__(self, config):
        self.url = config['url']
        self.ticket = config['ticket']
        self.palabras_clave = config['palabras_clave']
        self.stop_words = set(config['stop_words'])

    def normalizar_texto(self, texto):
        return texto.lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')

    def extraer(self):
        params = {
            "ticket": self.ticket,
            "estado": "activas",
        }
        try:
            response = requests.get(self.url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("Listado", [])
        except Exception as e:
            logging.error(f"Error al obtener licitaciones: {e}")
            return []

    def filtrar_licitaciones(self, licitaciones):
        encontrados = []
        for lic in licitaciones:
            nombre = self.normalizar_texto(lic.get("Nombre", ""))
            palabras_coincidentes = []
            
            for frase_original in self.palabras_clave:
                frase_normalizada = self.normalizar_texto(frase_original)
                # Buscar la frase completa en el nombre
                if frase_normalizada in nombre:
                    palabras_coincidentes.append(frase_original)
            
            if palabras_coincidentes:
                lic['palabras_coincidentes'] = palabras_coincidentes
                encontrados.append(lic)
        return encontrados
