# Contribution guidelines

The static website is generated from [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/) template using Python.
Information on this website are taken via [Home Assistant REST API](https://developers.home-assistant.io/docs/api/rest/).

## Env variables

- `TOKEN` - Home Assistant REST API access token

- `URL` - URL to the HS3 Home Assistant server

## Branch structure

🌿 `main` - this is the main development branch. If you want to introduce changes to the repository, you should open a PR on this branch.

🌿 `gh-pages` - the website is being deployed via GitHub Pages from this branch. All changes to this branch are implemented automatically via [Update website GitHub Action](https://github.com/MartaSien/home-assistant-hs3-plan/actions/workflows/update-website.yml). 🛑 Please don't add any changes to this branch manually. Instead, open a PR to the `main` branch.

## Tips on development

1. To avoid intellisense errors in `_layout.html` file I recommend [Better Jinja](https://marketplace.visualstudio.com/items?itemName=samuelcolvin.jinjahtml) plugin for Visual Studio Code and setting up this file as `Jinja HTML`.