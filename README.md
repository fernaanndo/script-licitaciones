# Extractor de Licitaciones - Mercado Público Chile

## Descripción

Este proyecto automatiza la búsqueda y filtrado de licitaciones activas del portal [Mercado Público de Chile](https://www.mercadopublico.cl/), enfocándose específicamente en oportunidades relacionadas con **educación técnica profesional** y áreas afines.

El sistema consulta la API oficial de Mercado Público, filtra las licitaciones que contienen palabras clave específicas y guarda los resultados en archivos JSON para su posterior análisis.

## Características

- 🔍 **Búsqueda automatizada** de licitaciones activas en tiempo real
- 🎯 **Filtrado inteligente** por palabras clave relacionadas con educación técnica
- 📊 **Exportación a JSON** con timestamp para control de versiones
- 🌐 **Normalización de texto** (manejo de tildes y mayúsculas/minúsculas)
- 📝 **Registro detallado** (logging) de operaciones

## Palabras Clave Monitoreadas

El sistema busca licitaciones que contengan términos relacionados con:

- Educación técnica profesional (ETP, EMTP)
- Formación dual y alternancia
- Competencias laborales
- Prácticas profesionales
- Metodologías activas (ABP, ABS)
- Tecnologías educativas (robótica, IA, Makerspaces, Fablab)
- Herramientas técnicas (BIM, Archicad, ERP, automatización)
- Certificaciones (WorldSkills, ISO)
- Vinculación con empresas
- Liderazgo pedagógico
- Convivencia escolar

## Estructura del Proyecto

```
.
├── main.py              # Script principal de ejecución
├── licitaciones.py      # Clase LicitacionesExtractor con lógica de extracción
├── config.json          # Configuración de palabras clave y URL de API
└── resultados/          # Carpeta donde se guardan los JSON (generada automáticamente)
```

## Requisitos

- Python 3.7+
- Biblioteca `requests`

## Instalación

1. Clonar o descargar el repositorio

2. Instalar las dependencias:
```bash
pip install requests
```

## Configuración

El archivo `config.json` contiene:

- **url**: Endpoint de la API de Mercado Público
- **palabras_clave**: Lista de términos a buscar en las licitaciones
- **stop_words**: Palabras comunes a ignorar en el procesamiento

Puedes modificar estas listas según tus necesidades específicas.

## Uso

Ejecutar el script principal:

```bash
python main.py
```

El programa:
1. Carga la configuración desde `config.json`
2. Consulta las licitaciones activas en la API de Mercado Público
3. Filtra las que contienen las palabras clave definidas
4. Guarda los resultados en `resultados/licitaciones_[TIMESTAMP].json`

## Formato de Salida

Los archivos JSON generados contienen cada licitación con:
- Todos los campos originales de la API
- Campo adicional `palabras_coincidentes`: lista de términos encontrados

Ejemplo de estructura:
```json
[
  {
    "Nombre": "Licitación de capacitación en educación técnica profesional",
    "CodigoExterno": "1234-56-LE21",
    "Estado": "Activa",
    "FechaCierre": "2026-03-15",
    "palabras_coincidentes": [
      "educación técnica profesional",
      "capacitación docente TP"
    ],
    ...
  }
]
```

## Logging

El sistema registra:
- ✅ Número de licitaciones encontradas
- ✅ Éxito/fallo en el guardado de archivos
- ❌ Errores en la conexión a la API
- ❌ Problemas al cargar configuración

## Notas Técnicas

- **Normalización**: El sistema normaliza texto eliminando tildes y convirtiendo a minúsculas para mejorar la detección
- **Ticket de API**: Utiliza un ticket fijo para autenticación con la API de Mercado Público
- **Estado de búsqueda**: Solo busca licitaciones en estado "activas"

## Contribución

Para agregar nuevas palabras clave, edita el array `palabras_clave` en `config.json`.

## Licencia

Este proyecto es de uso libre para fines educativos y de investigación.

---

**Nota**: Este proyecto utiliza la API pública de Mercado Público de Chile. Asegúrate de cumplir con los términos de uso del servicio.
