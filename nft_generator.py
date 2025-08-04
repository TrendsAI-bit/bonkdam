import os
import json
import random
from PIL import Image, ImageDraw, ImageFont
import hashlib
from datetime import datetime
import shutil

class BonkdamNFTGenerator:
    def __init__(self):
        self.base_images = []
        self.traits = {
            'helmet_type': ['Zaku', 'RX', 'Custom', 'Open Visor'],
            'armor_style': ['Gundam Suit', 'Tactical', 'Cyber Ronin', 'Bonkium Alloy'],
            'emblem': ['Bonk Crest', 'MemeSigil', 'Unknown Script'],
            'facial_expression': ['Blank', 'Furious', 'Glitched', 'LOL'],
            'weapon': ['Energy Blade', 'Bonk Rifle', 'Meme Drive Core', 'Dual Missiles'],
            'back_accessory': ['Jetpack', 'Banner', 'Katana', 'Antenna'],
            'background': ['Hangar', 'Mecha Forge', 'Upload Core', 'Bonk Battlefield']
        }
        
        self.rarity_distribution = {
            'Ultra Rare': 2,
            'Legendary': 10,
            'Epic': 38,
            'Rare': 150,
            'Uncommon': 300,
            'Common': 500
        }
        
        self.load_base_images()
        
    def load_base_images(self):
        """Load all base images from the asset folder"""
        asset_dir = "asset"
        for i in range(1, 17):
            img_path = os.path.join(asset_dir, f"{i}.png")
            if os.path.exists(img_path):
                self.base_images.append(img_path)
        print(f"Loaded {len(self.base_images)} base images")
    
    def generate_traits(self, rarity):
        """Generate traits based on rarity"""
        traits = {}
        
        # Common traits for all rarities
        traits['helmet_type'] = random.choice(self.traits['helmet_type'])
        traits['armor_style'] = random.choice(self.traits['armor_style'])
        traits['emblem'] = random.choice(self.traits['emblem'])
        traits['facial_expression'] = random.choice(self.traits['facial_expression'])
        traits['weapon'] = random.choice(self.traits['weapon'])
        traits['back_accessory'] = random.choice(self.traits['back_accessory'])
        traits['background'] = random.choice(self.traits['background'])
        
        # Rarity-specific modifications
        if rarity == 'Ultra Rare':
            # Ultra rare gets special traits
            traits['helmet_type'] = 'Command Core'
            traits['armor_style'] = 'Alpha Commander' if random.random() < 0.5 else 'Red Eye XO'
            traits['emblem'] = 'Bonk Crest'
            traits['facial_expression'] = 'Furious'
            traits['weapon'] = 'Meme Drive Core'
            traits['back_accessory'] = 'Jetpack'
            traits['background'] = 'Bonk Battlefield'
            
        elif rarity == 'Legendary':
            # Legendary gets glitch traits
            if random.random() < 0.3:
                traits['facial_expression'] = 'Glitched'
            if random.random() < 0.4:
                traits['armor_style'] = 'Cyber Ronin'
                
        elif rarity == 'Epic':
            # Epic gets Zaku-style helmets and Gundanium cores
            if random.random() < 0.6:
                traits['helmet_type'] = 'Zaku'
            if random.random() < 0.5:
                traits['armor_style'] = 'Gundam Suit'
                
        elif rarity == 'Rare':
            # Rare gets unique armor and alternate colors
            if random.random() < 0.4:
                traits['armor_style'] = 'Tactical'
            if random.random() < 0.3:
                traits['emblem'] = 'MemeSigil'
                
        elif rarity == 'Uncommon':
            # Uncommon gets distinct variations
            if random.random() < 0.5:
                traits['helmet_type'] = 'Custom'
            if random.random() < 0.4:
                traits['weapon'] = 'Dual Missiles'
                
        # Common keeps basic traits
        
        return traits
    
    def generate_nft(self, token_id, rarity):
        """Generate a single NFT"""
        # Select base image
        base_image_path = random.choice(self.base_images)
        
        # Generate traits
        traits = self.generate_traits(rarity)
        
        # Create metadata
        metadata = {
            "name": f"Bonkdam Unit-{token_id:04d}",
            "description": f"A unique Bonkdam NFT from the legendary collection. Rarity: {rarity}",
            "image": f"https://your-domain.com/images/{token_id}.png",
            "external_url": "https://your-domain.com",
            "attributes": [
                {"trait_type": "Rarity", "value": rarity},
                {"trait_type": "Helmet Type", "value": traits['helmet_type']},
                {"trait_type": "Armor Style", "value": traits['armor_style']},
                {"trait_type": "Emblem", "value": traits['emblem']},
                {"trait_type": "Facial Expression", "value": traits['facial_expression']},
                {"trait_type": "Weapon", "value": traits['weapon']},
                {"trait_type": "Back Accessory", "value": traits['back_accessory']},
                {"trait_type": "Background", "value": traits['background']}
            ],
            "properties": {
                "files": [
                    {
                        "uri": f"https://your-domain.com/images/{token_id}.png",
                        "type": "image/png"
                    }
                ],
                "category": "image"
            }
        }
        
        return {
            'token_id': token_id,
            'rarity': rarity,
            'base_image': base_image_path,
            'traits': traits,
            'metadata': metadata
        }
    
    def generate_collection(self):
        """Generate the entire 1000 NFT collection"""
        collection = []
        token_id = 1
        
        # Generate NFTs based on rarity distribution
        for rarity, count in self.rarity_distribution.items():
            print(f"Generating {count} {rarity} NFTs...")
            for i in range(count):
                nft = self.generate_nft(token_id, rarity)
                collection.append(nft)
                token_id += 1
        
        return collection
    
    def save_metadata(self, collection):
        """Save metadata for each NFT"""
        os.makedirs("metadata", exist_ok=True)
        
        for nft in collection:
            metadata_file = f"metadata/{nft['token_id']}.json"
            with open(metadata_file, 'w') as f:
                json.dump(nft['metadata'], f, indent=2)
        
        print(f"Saved metadata for {len(collection)} NFTs")
    
    def create_collection_summary(self, collection):
        """Create a summary of the collection"""
        summary = {
            "name": "Bonkdam NFT Collection",
            "description": "A legendary collection of 1000 unique Bonkdam NFTs",
            "total_supply": 1000,
            "rarity_distribution": self.rarity_distribution,
            "generated_at": datetime.now().isoformat(),
            "nfts": []
        }
        
        for nft in collection:
            summary['nfts'].append({
                'token_id': nft['token_id'],
                'name': nft['metadata']['name'],
                'rarity': nft['rarity'],
                'base_image': os.path.basename(nft['base_image'])
            })
        
        with open("collection_summary.json", 'w') as f:
            json.dump(summary, f, indent=2)
        
        print("Created collection summary")
    
    def generate_images(self, collection):
        """Generate the actual NFT images (placeholder for now)"""
        os.makedirs("images", exist_ok=True)
        
        for nft in collection:
            # For now, just copy the base image
            # In a real implementation, you'd layer traits on top
            src_path = nft['base_image']
            dst_path = f"images/{nft['token_id']}.png"
            shutil.copy2(src_path, dst_path)
        
        print(f"Generated {len(collection)} images")

def main():
    print("🚀 Starting Bonkdam NFT Collection Generation...")
    
    generator = BonkdamNFTGenerator()
    
    # Generate the collection
    collection = generator.generate_collection()
    
    # Save metadata
    generator.save_metadata(collection)
    
    # Create collection summary
    generator.create_collection_summary(collection)
    
    # Generate images
    generator.generate_images(collection)
    
    print("✅ NFT Collection Generation Complete!")
    print(f"📊 Generated {len(collection)} NFTs")
    print("📁 Files created:")
    print("  - metadata/ (contains individual NFT metadata)")
    print("  - images/ (contains NFT images)")
    print("  - collection_summary.json (overview of the collection)")

if __name__ == "__main__":
    main() 