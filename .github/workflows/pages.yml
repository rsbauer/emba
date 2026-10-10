name: Deploy Jekyll to GitHub Pages

on:
  push:
    branches:
      - main   # Change to 'master' if your default branch is master
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Prepare Staging Build
        run: python scripts/prepare_build.py

      - name: Build with Jekyll
        uses: actions/jekyll-build-pages@v1
        with:
          source: './_build_root'
          destination: './_site'

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4