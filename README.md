# Bonkdam NFT Collection Generator

A powerful NFT collection generator that creates 1000 unique Bonkdam NFTs with varying rarities and traits.

## 🎯 Collection Overview

**Total Supply:** 1,000 NFTs

### Rarity Distribution
- **Ultra Rare:** 2 NFTs (Command Core units)
- **Legendary:** 10 NFTs (Prototype Mecha with glitch traits)
- **Epic:** 38 NFTs (Elite Strike Force with Zaku helmets)
- **Rare:** 150 NFTs (Special Forces with unique armor)
- **Uncommon:** 300 NFTs (Frontline Infantry with distinct variations)
- **Common:** 500 NFTs (Standard Issue Troopers)

## 🧬 Trait System

### Core Traits
- **Helmet Type:** Zaku, RX, Custom, Open Visor
- **Armor Style:** Gundam Suit, Tactical, Cyber Ronin, Bonkium Alloy
- **Emblem:** Bonk Crest, MemeSigil, Unknown Script
- **Facial Expression:** Blank, Furious, Glitched, LOL
- **Weapon:** Energy Blade, Bonk Rifle, Meme Drive Core, Dual Missiles
- **Back Accessory:** Jetpack, Banner, Katana, Antenna
- **Background:** Hangar, Mecha Forge, Upload Core, Bonk Battlefield

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- 16 base images in the `asset/` folder (named 1.png through 16.png)

### Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Ensure your base images are in the `asset/` folder:
```
asset/
├── 1.png
├── 2.png
├── ...
└── 16.png
```

### Generate Collection

#### Basic Generator (Metadata Only)
```bash
python nft_generator.py
```

#### Advanced Generator (With Image Effects)
```bash
python advanced_nft_generator.py
```

## 📁 Output Structure

After generation, you'll have:

```
bonkdam/
├── metadata/           # Individual NFT metadata files
│   ├── 1.json
│   ├── 2.json
│   └── ...
├── images/            # Generated NFT images
│   ├── 1.png
│   ├── 2.png
│   └── ...
├── collection_summary.json  # Collection overview
├── asset/             # Your base images
└── *.py              # Generator scripts
```

## 🎨 Features

### Basic Generator (`nft_generator.py`)
- Generates metadata for all 1000 NFTs
- Creates collection summary
- Copies base images as placeholders

### Advanced Generator (`advanced_nft_generator.py`)
- All features from basic generator
- Applies visual effects based on rarity
- Color filters and glow effects
- Glitch effects for legendary NFTs
- Unique visual modifications per rarity

## 📊 Metadata Format

Each NFT metadata follows the OpenSea standard:

```json
{
  "name": "Bonkdam Unit-0001",
  "description": "A unique Bonkdam NFT from the legendary collection. Rarity: Ultra Rare",
  "image": "https://your-domain.com/images/1.png",
  "attributes": [
    {"trait_type": "Rarity", "value": "Ultra Rare"},
    {"trait_type": "Helmet Type", "value": "Command Core"},
    {"trait_type": "Armor Style", "value": "Alpha Commander"},
    // ... more traits
  ]
}
```

## 🎯 Rarity-Specific Features

### Ultra Rare (2 NFTs)
- Command Core helmets
- Alpha Commander or Red Eye XO armor
- Exclusive traits and visual effects
- Golden/platinum color schemes

### Legendary (10 NFTs)
- Prototype Mecha characteristics
- Glitch effects and Cyber Ronin armor
- Purple/cyan/neon color schemes
- Enhanced visual effects

### Epic (38 NFTs)
- Zaku-style helmets
- Gundam Suit armor
- Blue/red/green color schemes
- Subtle glow effects

### Rare (150 NFTs)
- Tactical armor styles
- MemeSigil emblems
- Orange/yellow/pink color schemes

### Uncommon (300 NFTs)
- Custom helmets
- Dual Missiles weapons
- Gray/brown/olive color schemes

### Common (500 NFTs)
- Standard variations
- Basic color schemes
- Core Bonk expressions

## 🔧 Customization

### Modify Rarity Distribution
Edit the `rarity_distribution` in the generator class:

```python
self.rarity_distribution = {
    'Ultra Rare': 2,
    'Legendary': 10,
    'Epic': 38,
    'Rare': 150,
    'Uncommon': 300,
    'Common': 500
}
```

### Add New Traits
Extend the `traits` dictionary:

```python
self.traits = {
    'helmet_type': ['Zaku', 'RX', 'Custom', 'Open Visor', 'NEW_TRAIT'],
    # ... other trait categories
}
```

### Customize Visual Effects
Modify the `apply_color_filter` and `add_rarity_effects` methods in the advanced generator.

## 🚀 Deployment

1. **Upload Images:** Host your generated images on IPFS or your preferred storage
2. **Update Metadata:** Replace image URLs in metadata files with your hosted URLs
3. **Deploy Smart Contract:** Use the metadata for your NFT smart contract
4. **Mint Collection:** Deploy your collection to your preferred blockchain

## 📝 Notes

- The basic generator creates metadata only
- The advanced generator adds visual effects to images
- All NFTs are unique with different trait combinations
- Rarity affects both traits and visual appearance
- Collection summary provides overview of all generated NFTs

## 🤝 Support

For questions or customization requests, please refer to the code comments or modify the generator classes as needed.

---

**Happy NFT Generation! 🚀** 