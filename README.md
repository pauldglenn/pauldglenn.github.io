# Personal Website

A static personal website built with Pelican, a Python-based static site generator.

## Setup

1. Install uv (if you haven't already):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create a virtual environment and install dependencies:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .
```

3. Clone the pelican-clean-blog theme and plugins:
```bash
git clone https://github.com/gilsondev/pelican-clean-blog.git themes/pelican-clean-blog
git clone --recursive https://github.com/getpelican/pelican-plugins.git plugins
```

4. Update your `pelicanconf.py` to include the plugins path:
```python
PLUGIN_PATHS = ['plugins']
PLUGINS = []  # Add specific plugins you want to use here
```

## Development

1. Start the development server:
```bash
pelican --listen
```

2. View your site at http://localhost:8000

## Building for Production

1. Generate the static site:
```bash
pelican content
```

2. The generated site will be in the `output` directory.

## Customization

- Edit `pelicanconf.py` to configure site settings
- Add content in the `content` directory
- Customize the theme in `themes/pelican-clean-blog`

## Deployment

The `output` directory contains the static files that can be deployed to any web hosting service that supports static websites, such as:
- GitHub Pages
- Netlify
- Vercel
- Amazon S3 