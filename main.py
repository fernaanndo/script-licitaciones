import logging
import json
import os
from datetime import datetime
from licitaciones import LicitacionesExtractor


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def cargar_configuracion(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        raise RuntimeError(f"Error al cargar el archivo de configuración '{path}': {e}")


def guardar_json_local(licitaciones, carpeta='resultados'):
    """
    Guarda las licitaciones en un archivo JSON local.
    """
    try:
        # Crear la carpeta si no existe
        os.makedirs(carpeta, exist_ok=True)
        
        # Generar nombre de archivo con timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        nombre_archivo = f'licitaciones_{timestamp}.json'
        ruta_completa = os.path.join(carpeta, nombre_archivo)
        
        # Guardar el JSON
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            json.dump(licitaciones, f, ensure_ascii=False, indent=2)
        
        logging.info(f"JSON guardado exitosamente en: {ruta_completa}")
        return True
    except Exception as e:
        logging.error(f"Error al guardar el JSON: {e}")
        return False


def main():
    config = cargar_configuracion('config.json')

    ticket = "5BBEF888-36CA-4B67-8E57-84FE81D74692"
    if not ticket:
        raise EnvironmentError('Variable de entorno TICKET no encontrada.')

    config['ticket'] = ticket

    extractor = LicitacionesExtractor(config)
    licitaciones = extractor.extraer()
    encontrados = extractor.filtrar_licitaciones(licitaciones)

    if not encontrados:
        raise RuntimeError("No se encontraron licitaciones que cumplan los filtros definidos.")

    # Guardar las licitaciones en un archivo JSON local
    guardado_exitoso = guardar_json_local(encontrados)
    if not guardado_exitoso:
        raise RuntimeError("Error al guardar el JSON localmente.")

    logging.info(f"Se encontraron {len(encontrados)} licitaciones y se guardaron exitosamente.")



if __name__ == "__main__":
    main()
