#!/usr/bin/env python3
"""
Test script for the Bonkdam NFT Generator
This script demonstrates the generator functionality with a small sample.
"""

import os
import json
from nft_generator import BonkdamNFTGenerator
from advanced_nft_generator import AdvancedBonkdamNFTGenerator

def test_basic_generator():
    """Test the basic NFT generator with a small sample"""
    print("🧪 Testing Basic NFT Generator...")
    
    # Create a test generator with reduced numbers
    generator = BonkdamNFTGenerator()
    generator.rarity_distribution = {
        'Ultra Rare': 1,
        'Legendary': 2,
        'Epic': 3,
        'Rare': 4,
        'Uncommon': 5,
        'Common': 5
    }
    
    # Generate a small collection
    collection = generator.generate_collection()
    
    # Save test metadata
    os.makedirs("test_metadata", exist_ok=True)
    for nft in collection:
        metadata_file = f"test_metadata/{nft['token_id']}.json"
        with open(metadata_file, 'w') as f:
            json.dump(nft['metadata'], f, indent=2)
    
    print(f"✅ Generated {len(collection)} test NFTs")
    print("📁 Test metadata saved in test_metadata/ folder")
    
    # Show sample metadata
    if collection:
        sample_nft = collection[0]
        print(f"\n📋 Sample NFT Metadata:")
        print(f"Name: {sample_nft['metadata']['name']}")
        print(f"Rarity: {sample_nft['rarity']}")
        print(f"Traits: {sample_nft['traits']}")

def test_advanced_generator():
    """Test the advanced NFT generator with visual effects"""
    print("\n🧪 Testing Advanced NFT Generator...")
    
    # Create a test generator with reduced numbers
    generator = AdvancedBonkdamNFTGenerator()
    generator.rarity_distribution = {
        'Ultra Rare': 1,
        'Legendary': 2,
        'Epic': 3,
        'Rare': 4,
        'Uncommon': 5,
        'Common': 5
    }
    
    # Generate a small collection
    collection = generator.generate_collection()
    
    # Save test images
    os.makedirs("test_images", exist_ok=True)
    for nft in collection:
        image_path = f"test_images/{nft['token_id']}.png"
        nft['image'].save(image_path, 'PNG')
    
    print(f"✅ Generated {len(collection)} test NFTs with visual effects")
    print("📁 Test images saved in test_images/ folder")

def show_collection_stats():
    """Show statistics about the full collection"""
    print("\n📊 Full Collection Statistics:")
    
    generator = BonkdamNFTGenerator()
    total = sum(generator.rarity_distribution.values())
    
    print(f"Total NFTs: {total}")
    print("Rarity Distribution:")
    for rarity, count in generator.rarity_distribution.items():
        percentage = (count / total) * 100
        print(f"  {rarity}: {count} NFTs ({percentage:.1f}%)")
    
    print(f"\nTrait Categories: {len(generator.traits)}")
    for category, traits in generator.traits.items():
        print(f"  {category}: {len(traits)} options")

def main():
    """Run all tests"""
    print("🚀 Bonkdam NFT Generator Test Suite")
    print("=" * 50)
    
    # Check if base images exist
    asset_dir = "asset"
    if not os.path.exists(asset_dir):
        print("❌ Error: asset/ folder not found!")
        print("Please ensure you have 16 base images (1.png through 16.png) in the asset/ folder")
        return
    
    base_images = [f for f in os.listdir(asset_dir) if f.endswith('.png')]
    if len(base_images) < 16:
        print(f"⚠️  Warning: Found {len(base_images)} images, expected 16")
    else:
        print(f"✅ Found {len(base_images)} base images")
    
    # Run tests
    try:
        test_basic_generator()
        test_advanced_generator()
        show_collection_stats()
        
        print("\n🎉 All tests completed successfully!")
        print("\nTo generate the full collection:")
        print("  python nft_generator.py          # Basic (metadata only)")
        print("  python advanced_nft_generator.py # Advanced (with effects)")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")

if __name__ == "__main__":
    main() 