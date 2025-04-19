AUTHOR = 'Paul Glenn'
SITENAME = 'Paul Glenn'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

# Use index.html as landing page
INDEX_SAVE_AS = 'index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
ARTICLE_URL = 'articles/{slug}/'
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('GitHub', 'https://github.com/pdglenn'),
    ('LinkedIn', 'https://linkedin.com/in/pauldglenn'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/pdglenn'),
)

DEFAULT_PAGINATION = 10

# Theme settings
THEME = 'themes/pelican-clean-blog'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARCHIVES_ON_MENU = True

# Static files
STATIC_PATHS = ['images']

# Plugin settings
PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'sitemap',           # Generates sitemap.xml for SEO
    'neighbors',         # Adds next/previous article navigation
    'related_posts',     # Shows related articles
    'series',            # Groups articles into series
]

# Sitemap settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Direct templates
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']

# Enable document-relative URLs when developing
RELATIVE_URLS = True 