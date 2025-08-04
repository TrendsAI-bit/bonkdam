import os
import json
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import hashlib
from datetime import datetime
import shutil
import numpy as np

class AdvancedBonkdamNFTGenerator:
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
        
        # Color variations for different rarities
        self.color_schemes = {
            'Ultra Rare': ['gold', 'platinum'],
            'Legendary': ['purple', 'cyan', 'neon'],
            'Epic': ['blue', 'red', 'green'],
            'Rare': ['orange', 'yellow', 'pink'],
            'Uncommon': ['gray', 'brown', 'olive'],
            'Common': ['white', 'black', 'gray']
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
    
    def apply_color_filter(self, image, color_scheme):
        """Apply color filters based on rarity"""
        if color_scheme == 'gold':
            # Apply golden filter
            enhancer = ImageEnhance.Color(image)
            image = enhancer.enhance(1.5)
            enhancer = ImageEnhance.Brightness(image)
            image = enhancer.enhance(1.2)
        elif color_scheme == 'platinum':
            # Apply platinum filter
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(1.3)
        elif color_scheme == 'neon':
            # Apply neon glow effect
            image = image.filter(ImageFilter.GaussianBlur(1))
            enhancer = ImageEnhance.Brightness(image)
            image = enhancer.enhance(1.4)
        elif color_scheme == 'glitch':
            # Apply glitch effect
            width, height = image.size
            pixels = image.load()
            for x in range(0, width, 10):
                for y in range(height):
                    if random.random() < 0.1:
                        pixels[x, y] = (255, 0, 255)  # Magenta glitch
        
        return image
    
    def add_rarity_effects(self, image, rarity):
        """Add visual effects based on rarity"""
        if rarity == 'Ultra Rare':
            # Add golden glow
            glow = image.copy()
            glow = glow.filter(ImageFilter.GaussianBlur(10))
            enhancer = ImageEnhance.Brightness(glow)
            glow = enhancer.enhance(1.5)
            image = Image.alpha_composite(glow.convert('RGBA'), image.convert('RGBA'))
            
        elif rarity == 'Legendary':
            # Add purple glow
            glow = image.copy()
            glow = glow.filter(ImageFilter.GaussianBlur(5))
            enhancer = ImageEnhance.Color(glow)
            glow = enhancer.enhance(1.3)
            image = Image.alpha_composite(glow.convert('RGBA'), image.convert('RGBA'))
            
        elif rarity == 'Epic':
            # Add subtle glow
            glow = image.copy()
            glow = glow.filter(ImageFilter.GaussianBlur(3))
            enhancer = ImageEnhance.Brightness(glow)
            glow = enhancer.enhance(1.2)
            image = Image.alpha_composite(glow.convert('RGBA'), image.convert('RGBA'))
        
        return image
    
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
            traits['helmet_type'] = 'Command Core'
            traits['armor_style'] = 'Alpha Commander' if random.random() < 0.5 else 'Red Eye XO'
            traits['emblem'] = 'Bonk Crest'
            traits['facial_expression'] = 'Furious'
            traits['weapon'] = 'Meme Drive Core'
            traits['back_accessory'] = 'Jetpack'
            traits['background'] = 'Bonk Battlefield'
            
        elif rarity == 'Legendary':
            if random.random() < 0.3:
                traits['facial_expression'] = 'Glitched'
            if random.random() < 0.4:
                traits['armor_style'] = 'Cyber Ronin'
                
        elif rarity == 'Epic':
            if random.random() < 0.6:
                traits['helmet_type'] = 'Zaku'
            if random.random() < 0.5:
                traits['armor_style'] = 'Gundam Suit'
                
        elif rarity == 'Rare':
            if random.random() < 0.4:
                traits['armor_style'] = 'Tactical'
            if random.random() < 0.3:
                traits['emblem'] = 'MemeSigil'
                
        elif rarity == 'Uncommon':
            if random.random() < 0.5:
                traits['helmet_type'] = 'Custom'
            if random.random() < 0.4:
                traits['weapon'] = 'Dual Missiles'
        
        return traits
    
    def create_nft_image(self, base_image_path, rarity, traits):
        """Create the actual NFT image with effects"""
        # Load base image
        image = Image.open(base_image_path)
        
        # Apply rarity-specific color scheme
        color_scheme = random.choice(self.color_schemes[rarity])
        image = self.apply_color_filter(image, color_scheme)
        
        # Add rarity effects
        image = self.add_rarity_effects(image, rarity)
        
        # Add trait-based visual modifications
        if traits['facial_expression'] == 'Glitched':
            image = self.apply_color_filter(image, 'glitch')
        
        # Ensure image is in RGB mode
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        return image
    
    def generate_nft(self, token_id, rarity):
        """Generate a single NFT"""
        # Select base image
        base_image_path = random.choice(self.base_images)
        
        # Generate traits
        traits = self.generate_traits(rarity)
        
        # Create the NFT image
        nft_image = self.create_nft_image(base_image_path, rarity, traits)
        
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
            'metadata': metadata,
            'image': nft_image
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
    
    def save_images(self, collection):
        """Save the generated NFT images"""
        os.makedirs("images", exist_ok=True)
        
        for nft in collection:
            image_path = f"images/{nft['token_id']}.png"
            nft['image'].save(image_path, 'PNG')
        
        print(f"Saved {len(collection)} NFT images")
    
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

def main():
    print("🚀 Starting Advanced Bonkdam NFT Collection Generation...")
    
    generator = AdvancedBonkdamNFTGenerator()
    
    # Generate the collection
    collection = generator.generate_collection()
    
    # Save metadata
    generator.save_metadata(collection)
    
    # Save images
    generator.save_images(collection)
    
    # Create collection summary
    generator.create_collection_summary(collection)
    
    print("✅ Advanced NFT Collection Generation Complete!")
    print(f"📊 Generated {len(collection)} NFTs")
    print("📁 Files created:")
    print("  - metadata/ (contains individual NFT metadata)")
    print("  - images/ (contains NFT images with effects)")
    print("  - collection_summary.json (overview of the collection)")

if __name__ == "__main__":
    main() 