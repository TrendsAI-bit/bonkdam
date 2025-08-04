#!/usr/bin/env python3
"""
Collection Statistics Analyzer
Analyzes the generated Bonkdam NFT collection and provides detailed statistics.
"""

import json
import os
from collections import Counter, defaultdict

def analyze_collection():
    """Analyze the generated NFT collection"""
    print("📊 Bonkdam NFT Collection Analysis")
    print("=" * 50)
    
    # Load collection summary
    with open("collection_summary.json", "r") as f:
        summary = json.load(f)
    
    # Load all metadata files
    metadata_dir = "metadata"
    all_nfts = []
    
    for filename in os.listdir(metadata_dir):
        if filename.endswith('.json'):
            with open(os.path.join(metadata_dir, filename), 'r') as f:
                nft_data = json.load(f)
                all_nfts.append(nft_data)
    
    print(f"📈 Collection Overview:")
    print(f"   Total NFTs: {summary['total_supply']}")
    print(f"   Generated: {summary['generated_at']}")
    
    # Rarity analysis
    print(f"\n🎯 Rarity Distribution:")
    rarity_counts = Counter()
    for nft in all_nfts:
        for attr in nft['attributes']:
            if attr['trait_type'] == 'Rarity':
                rarity_counts[attr['value']] += 1
                break
    
    for rarity, count in rarity_counts.most_common():
        percentage = (count / len(all_nfts)) * 100
        print(f"   {rarity}: {count} NFTs ({percentage:.1f}%)")
    
    # Trait analysis
    print(f"\n🧬 Trait Analysis:")
    trait_counts = defaultdict(Counter)
    
    for nft in all_nfts:
        for attr in nft['attributes']:
            if attr['trait_type'] != 'Rarity':
                trait_counts[attr['trait_type']][attr['value']] += 1
    
    for trait_type, values in trait_counts.items():
        print(f"\n   {trait_type}:")
        for value, count in values.most_common():
            percentage = (count / len(all_nfts)) * 100
            print(f"     {value}: {count} ({percentage:.1f}%)")
    
    # Rarity-specific trait analysis
    print(f"\n🎨 Rarity-Specific Traits:")
    rarity_traits = defaultdict(lambda: defaultdict(Counter))
    
    for nft in all_nfts:
        rarity = None
        for attr in nft['attributes']:
            if attr['trait_type'] == 'Rarity':
                rarity = attr['value']
                break
        
        if rarity:
            for attr in nft['attributes']:
                if attr['trait_type'] != 'Rarity':
                    rarity_traits[rarity][attr['trait_type']][attr['value']] += 1
    
    for rarity in ['Ultra Rare', 'Legendary', 'Epic', 'Rare', 'Uncommon', 'Common']:
        if rarity in rarity_traits:
            print(f"\n   {rarity}:")
            for trait_type, values in rarity_traits[rarity].items():
                most_common = values.most_common(1)[0]
                print(f"     {trait_type}: {most_common[0]} ({most_common[1]} NFTs)")
    
    # Uniqueness analysis
    print(f"\n🔍 Uniqueness Analysis:")
    trait_combinations = Counter()
    
    for nft in all_nfts:
        traits = []
        for attr in nft['attributes']:
            if attr['trait_type'] != 'Rarity':
                traits.append(f"{attr['trait_type']}:{attr['value']}")
        trait_combinations[tuple(sorted(traits))] += 1
    
    unique_combinations = len(trait_combinations)
    print(f"   Unique trait combinations: {unique_combinations}")
    print(f"   Duplicate combinations: {len(all_nfts) - unique_combinations}")
    
    # Most common combinations
    print(f"\n🏆 Most Common Trait Combinations:")
    for combo, count in trait_combinations.most_common(5):
        if count > 1:
            print(f"   {count} NFTs with:")
            for trait in combo:
                print(f"     {trait}")
    
    # File structure
    print(f"\n📁 Generated Files:")
    metadata_count = len([f for f in os.listdir(metadata_dir) if f.endswith('.json')])
    images_dir = "images"
    if os.path.exists(images_dir):
        image_count = len([f for f in os.listdir(images_dir) if f.endswith('.png')])
        print(f"   Metadata files: {metadata_count}")
        print(f"   Image files: {image_count}")
    
    print(f"\n✅ Analysis Complete!")

if __name__ == "__main__":
    analyze_collection() 