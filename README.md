# Paul Glenn's Personal Website

This is my personal website built with Pelican, a static site generator written in Python. The site is hosted on GitHub Pages at [pdglenn.com](https://pdglenn.com).

## Features

- Clean, responsive design using the [Clean Blog](https://github.com/gilsondev/pelican-clean-blog) theme
- Blog articles and pages
- Custom domain (pdglenn.com)
- Automated deployment with GitHub Actions
- SEO optimization with sitemap
- Related posts and article series support

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/pauldglenn/pauldglenn.github.io.git
   cd pauldglenn.github.io
   ```

2. Set up the Python environment using `uv`:
   ```bash
   uv venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

4. Build the site:
   ```bash
   PYTHONPATH=$PYTHONPATH:. pelican content -s publishconf.py
   ```

5. Preview locally:
   ```bash
   PYTHONPATH=$PYTHONPATH:. pelican --listen
   ```

## Project Structure

- `content/`: Source content (articles, pages, images)
- `output/`: Generated site (not tracked in git)
- `pelicanconf.py`: Development settings
- `publishconf.py`: Production settings
- `requirements.txt`: Python dependencies
- `.github/workflows/`: GitHub Actions configuration

## Dependencies

- Python 3.10+
- Pelican 4.8.0
- Markdown 3.4.1
- Typogrify 2.0.7
- Various Pelican plugins (sitemap, neighbors, related_posts, series)

## Deployment

The site is automatically deployed to GitHub Pages using GitHub Actions when changes are pushed to the `main` branch. The workflow:

1. Checks out the repository
2. Sets up Python
3. Installs dependencies
4. Builds the site
5. Deploys to the `gh-pages` branch

## Custom Domain

The site uses a custom domain (pdglenn.com) configured through:

1. DNS A records pointing to GitHub Pages
2. CNAME file in the `gh-pages` branch
3. GitHub Pages custom domain settings

## Development

To add new content:

1. Create articles in `content/articles/`
2. Create pages in `content/pages/`
3. Add images to `content/images/`

To modify the theme or configuration:

1. Update `pelicanconf.py` for development settings
2. Update `publishconf.py` for production settings
3. Customize theme files in `themes/pelican-clean-blog/`

## License

This project is licensed under the MIT License - see the LICENSE file for details. 