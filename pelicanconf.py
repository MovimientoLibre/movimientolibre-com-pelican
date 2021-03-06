#!/usr/bin/env python

# Para desarrollo
SITEURL = 'http://localhost:8000'
RELATIVE_URLS = False

# Sitio web
SITENAME = 'Movimiento Libre'
SITELOGO = 'theme/images/movimientolibre.png'
SITEDESCRIPTION = 'Plataforma de divulgación de conocimiento'
SITETWITTER = '@guivaloz'

# Autor
AUTHOR = 'Guillermo Valdés Lozano (guivaloz)'

# Directorio donde esta el contenido
PATH = 'content'

# Directorios que tienen los articulos
ARTICLE_PATHS = [
    'apuntes',
    'articulos',
    'presentaciones',
]

# Directorios que tienen páginas fijas, no artículos
PAGE_PATHS = [
    'licencias',
    'portafolio',
]

# Directorios y archivos que son fijos
# Agregue también los directorios que tienen archivos para artículos y páginas
STATIC_PATHS = [
    'CNAME',
    'favicon.ico',
    'LICENSE',
    'README.md',
    'robots.txt',
    'apuntes',
    'articulos',
    'presentaciones',
    'portafolio',
]

# Encabezados para las categorías
CATEGORIES_TITLES = {
    'apuntes': 'Apuntes',
    'articulos': 'Artículos',
    'presentaciones': 'Presentaciones',
}

# Usar el nombre del directorio como la categoría
USE_FOLDER_AS_CATEGORY = False

# Los artículos van en directorios por categoria/titulo/
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# Las páginas fijas van en directorios categoria/titulo/
PAGE_URL = '{category}/{slug}/'
PAGE_SAVE_AS = '{category}/{slug}/index.html'

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican_javascript']

# Plugin articles_list_json, add 'articles_lists_json' to PLUGINS
# ARTICLES_LISTS_JSON_OUTPUT_PATH = 'json'
# ARTICLES_LISTS_JSON_OUTPUT_ALL = 'all.json'
# ARTICLES_LISTS_JSON_CATEGORIES_FILTERS = None
# ARTICLES_LISTS_JSON_LIMIT = None

# Tema
THEME = 'themes/bs5'

# Lenguaje y zona horaria
DEFAULT_LANG = 'es'
TIMEZONE = 'America/Mexico_City'

# Para desarrollo, se desactiva la paginacion
DEFAULT_PAGINATION = False

# Para desarrollo, borrar todo output
DELETE_OUTPUT_DIRECTORY = True

# Siempre aprovechar lo que se tenga en caché
LOAD_CONTENT_CACHE = True

# Para desarrollo se desactiva la generacion de feeds
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Para desarrollo se desactivan los servicios de terceros, como Google Analytics y Search
USE_REMOTE_SERVICES = False
