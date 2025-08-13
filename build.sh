#!/bin/bash

# Build Jekyll site
echo "Building Jekyll site..."
bundle exec jekyll build

# Check if pagefind is installed
if command -v pagefind &> /dev/null; then
    echo "Generating pagefind index..."
    pagefind --source _site
    echo "Pagefind index generated!"
else
    echo "Pagefind not found. Please install pagefind to generate search index."
    echo "Install with: npm install -g pagefind"
fi

echo "Build complete!"
