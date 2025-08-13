# Ibiza Real Estate Jekyll Website

A Jekyll-based website for displaying Ibiza real estate listings with search functionality powered by Pagefind.

## Features

- 🏠 Property listings with detailed information
- 🔍 Full-text search with Pagefind
- 📱 Responsive design with Bootstrap
- 🚀 Automatic deployment to GitHub Pages
- 📊 Dynamic data from JSON files

## Local Development

### Prerequisites

- Ruby 3.3+
- Node.js 18+
- Bundler

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ibiza-realestate-jekyll
   ```

2. **Install Ruby dependencies**
   ```bash
   bundle install
   ```

3. **Install Node.js dependencies**
   ```bash
   npm install
   ```

4. **Build the site**
   ```bash
   npm run build-full
   ```

5. **Serve locally**
   ```bash
   npm run serve
   ```

## Deployment

This site is automatically deployed to GitHub Pages using GitHub Actions. The workflow:

1. Builds the Jekyll site
2. Generates the Pagefind search index
3. Deploys to GitHub Pages

### Manual Deployment

To manually build and deploy:

```bash
# Build the site
npm run build

# Generate search index
npm run search

# Or do both at once
npm run build-full
```

## Data Structure

Property data is stored in `_data/listings.json` with the following structure:

```json
{
  "property_id": "unique-id",
  "name": "Property Name",
  "current_price": 1500000,
  "bedroom": 4,
  "bathroom": 3,
  "living_area": 200,
  "region": "Ibiza",
  "sub_region": "Santa Eulalia",
  "type": "House",
  "status": "sale",
  "agency": "Agency Name"
}
```

## Search Configuration

The site uses Pagefind for search functionality. The search index is automatically generated during the build process and includes:

- Property names and descriptions
- Location information
- Property details (bedrooms, bathrooms, etc.)
- Filterable by region, type, status, and more

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally with `npm run build-full`
5. Submit a pull request

## License

[Add your license here]
