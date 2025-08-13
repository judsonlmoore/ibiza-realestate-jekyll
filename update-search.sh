#!/bin/bash

# Check if pagefind is installed
if command -v pagefind &> /dev/null; then
    echo "Updating pagefind search index..."
    pagefind --source _site
    echo "Search index updated!"
else
    echo "Pagefind not found. Please install pagefind to generate search index."
    echo "Install with: npm install -g pagefind"
fi
