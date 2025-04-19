from pelicanconf import *

# Production settings
SITEURL = 'https://pdglenn.com'  # Your domain
RELATIVE_URLS = False

# Feed settings
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Delete output directory before generating new files
DELETE_OUTPUT_DIRECTORY = True

# Enable caching
LOAD_CONTENT_CACHE = True
CACHE_CONTENT = True
CACHE_PATH = 'cache'

# Optimize images
IMAGE_PROCESS = {
    'article-image': {
        'type': 'responsive-image',
        'sizes': [
            (800, 600),
            (400, 300),
            (200, 150),
        ],
        'srcset': [
            (800, 'large'),
            (400, 'medium'),
            (200, 'small'),
        ],
    },
    'thumb': {
        'type': 'image',
        'width': 200,
        'height': 200,
        'crop': 'center',
    },
} 