#!/bin/bash

# Bonkdam Shōtaigun Website Deployment Script
# Pixel Platoon of the Meme Mechs

echo "🚀 Deploying Bonkdam Shōtaigun Website..."

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI not found. Installing..."
    npm install -g vercel
fi

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "❌ index.html not found. Please run this script from the website directory."
    exit 1
fi

# Check if images directory exists
if [ ! -d "images" ]; then
    echo "⚠️  Warning: images/ directory not found. Creating placeholder..."
    mkdir -p images
    echo "📁 Created images/ directory. Please add your NFT images."
fi

# Deploy to Vercel
echo "📤 Deploying to Vercel..."
vercel --prod

echo "✅ Deployment complete!"
echo "🌐 Your website is now live!"
echo "📝 Check the output above for your deployment URL." 