// Bonkdam Shōtaigun Website JavaScript
// Pixel Platoon of the Meme Mechs

// Global variables
let currentFilter = 'all';
let galleryData = [];
let walletConnected = false;

// DOM Elements
const loading = document.getElementById('loading');
const galleryGrid = document.getElementById('gallery-grid');
const filterButtons = document.querySelectorAll('.filter-btn');
const navLinks = document.querySelectorAll('.nav-link');
const walletBtn = document.getElementById('wallet-connect-btn');
const walletModal = document.getElementById('wallet-modal');
const featuredNftImg = document.getElementById('featured-nft-img');

// Initialize the website
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Initializing Bonkdam Shōtaigun Division...');
    
    // Hide loading screen after a delay
    setTimeout(() => {
        loading.classList.add('hidden');
        setTimeout(() => {
            loading.style.display = 'none';
        }, 500);
    }, 2000);
    
    // Initialize components
    initializeNavigation();
    initializeGallery();
    initializeWallet();
    initializeAnimations();
    
    console.log('✅ Division initialization complete!');
});

// Navigation functionality
function initializeNavigation() {
    // Smooth scrolling for navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth'
                });
                
                // Update active nav link
                navLinks.forEach(l => l.classList.remove('active'));
                this.classList.add('active');
            }
        });
    });
    
    // Update active nav link on scroll
    window.addEventListener('scroll', function() {
        const sections = document.querySelectorAll('section');
        const scrollPos = window.scrollY + 100;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            
            if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    });
}

// Gallery functionality
function initializeGallery() {
    // Load gallery data
    loadGalleryData();
    
    // Initialize filter buttons
    filterButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const filter = this.getAttribute('data-filter');
            setActiveFilter(filter);
            filterGallery(filter);
        });
    });
}

function loadGalleryData() {
    // Simulate loading gallery data from the collection
    // In a real implementation, this would load from your metadata
    galleryData = [];
    
    // Generate sample gallery items based on the 1000 NFT collection
    for (let i = 1; i <= 50; i++) { // Show first 50 for demo
        const rarity = getRarityForToken(i);
        galleryData.push({
            id: i,
            name: `Bonkdam Unit-${i.toString().padStart(4, '0')}`,
            image: `images/${i}.png`,
            rarity: rarity,
            traits: generateTraitsForToken(i, rarity)
        });
    }
    
    renderGallery();
}

function getRarityForToken(tokenId) {
    if (tokenId <= 2) return 'ultra-rare';
    if (tokenId <= 12) return 'legendary';
    if (tokenId <= 50) return 'epic';
    if (tokenId <= 200) return 'rare';
    if (tokenId <= 500) return 'uncommon';
    return 'common';
}

function generateTraitsForToken(tokenId, rarity) {
    const traits = {
        'helmet_type': ['Zaku', 'RX', 'Custom', 'Open Visor', 'Command Core'],
        'armor_style': ['Gundam Suit', 'Tactical', 'Cyber Ronin', 'Bonkium Alloy', 'Alpha Commander'],
        'emblem': ['Bonk Crest', 'MemeSigil', 'Unknown Script'],
        'facial_expression': ['Blank', 'Furious', 'Glitched', 'LOL'],
        'weapon': ['Energy Blade', 'Bonk Rifle', 'Meme Drive Core', 'Dual Missiles'],
        'back_accessory': ['Jetpack', 'Banner', 'Katana', 'Antenna'],
        'background': ['Hangar', 'Mecha Forge', 'Upload Core', 'Bonk Battlefield']
    };
    
    return {
        helmet: traits.helmet_type[Math.floor(Math.random() * traits.helmet_type.length)],
        armor: traits.armor_style[Math.floor(Math.random() * traits.armor_style.length)],
        emblem: traits.emblem[Math.floor(Math.random() * traits.emblem.length)],
        expression: traits.facial_expression[Math.floor(Math.random() * traits.facial_expression.length)],
        weapon: traits.weapon[Math.floor(Math.random() * traits.weapon.length)],
        accessory: traits.back_accessory[Math.floor(Math.random() * traits.back_accessory.length)],
        background: traits.background[Math.floor(Math.random() * traits.background.length)]
    };
}

function renderGallery() {
    if (!galleryGrid) return;
    
    galleryGrid.innerHTML = '';
    
    galleryData.forEach(item => {
        const card = createNFTCard(item);
        galleryGrid.appendChild(card);
    });
}

function createNFTCard(item) {
    const card = document.createElement('div');
    card.className = 'nft-card';
    card.setAttribute('data-rarity', item.rarity);
    
    card.innerHTML = `
        <div class="nft-image">
            <img src="${item.image}" alt="${item.name}" onload="this.parentElement.classList.add('loaded')" onerror="this.parentElement.innerHTML='<div class=\"nft-placeholder\">Loading...</div>'">
        </div>
        <div class="nft-info">
            <div class="nft-number">#${item.id.toString().padStart(4, '0')}</div>
            <div class="nft-name">${item.name}</div>
            <div class="nft-rarity ${item.rarity}">${item.rarity.replace('-', ' ').toUpperCase()}</div>
        </div>
    `;
    
    // Add click event to show details
    card.addEventListener('click', () => {
        showNFTDetails(item);
    });
    
    return card;
}

function setActiveFilter(filter) {
    currentFilter = filter;
    
    // Update filter button states
    filterButtons.forEach(btn => {
        btn.classList.remove('active');
        if (btn.getAttribute('data-filter') === filter) {
            btn.classList.add('active');
        }
    });
}

function filterGallery(filter) {
    const cards = document.querySelectorAll('.nft-card');
    
    cards.forEach(card => {
        const rarity = card.getAttribute('data-rarity');
        
        if (filter === 'all' || rarity === filter) {
            card.style.display = 'block';
            card.style.animation = 'fadeIn 0.5s ease-in-out';
        } else {
            card.style.display = 'none';
        }
    });
}

function showNFTDetails(item) {
    // Create a modal to show NFT details
    const modal = document.createElement('div');
    modal.className = 'nft-modal';
    modal.innerHTML = `
        <div class="modal-overlay"></div>
        <div class="modal-content">
            <button class="modal-close" onclick="this.parentElement.parentElement.remove()">
                <i class="fas fa-times"></i>
            </button>
            <div class="modal-body">
                <div class="nft-detail-image">
                    <img src="${item.image}" alt="${item.name}">
                </div>
                <div class="nft-detail-info">
                    <h3>${item.name}</h3>
                    <p class="rarity">${item.rarity.replace('-', ' ').toUpperCase()}</p>
                    <div class="traits">
                        <h4>Traits:</h4>
                        <div class="trait-grid">
                            <div class="trait-item">
                                <span class="trait-label">Helmet:</span>
                                <span class="trait-value">${item.traits.helmet}</span>
                            </div>
                            <div class="trait-item">
                                <span class="trait-label">Armor:</span>
                                <span class="trait-value">${item.traits.armor}</span>
                            </div>
                            <div class="trait-item">
                                <span class="trait-label">Emblem:</span>
                                <span class="trait-value">${item.traits.emblem}</span>
                            </div>
                            <div class="trait-item">
                                <span class="trait-label">Expression:</span>
                                <span class="trait-value">${item.traits.expression}</span>
                            </div>
                            <div class="trait-item">
                                <span class="trait-label">Weapon:</span>
                                <span class="trait-value">${item.traits.weapon}</span>
                            </div>
                            <div class="trait-item">
                                <span class="trait-label">Accessory:</span>
                                <span class="trait-value">${item.traits.accessory}</span>
                            </div>
                            <div class="trait-item">
                                <span class="trait-label">Background:</span>
                                <span class="trait-value">${item.traits.background}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    
    // Add modal styles
    const style = document.createElement('style');
    style.textContent = `
        .nft-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10000;
        }
        .nft-modal .modal-content {
            background: var(--medium-bg);
            border: var(--pixel-border);
            border-radius: 8px;
            padding: 2rem;
            max-width: 600px;
            width: 90%;
            max-height: 80vh;
            overflow-y: auto;
        }
        .nft-detail-image {
            text-align: center;
            margin-bottom: 2rem;
        }
        .nft-detail-image img {
            max-width: 100%;
            max-height: 300px;
            border: var(--pixel-border);
            border-radius: 8px;
        }
        .trait-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }
        .trait-item {
            display: flex;
            justify-content: space-between;
            padding: 0.5rem;
            background: var(--dark-bg);
            border-radius: 4px;
        }
        .trait-label {
            color: var(--text-muted);
            font-weight: 700;
        }
        .trait-value {
            color: var(--chrome);
            font-weight: 700;
        }
    `;
    document.head.appendChild(style);
}

// Wallet functionality
function initializeWallet() {
    if (walletBtn) {
        walletBtn.addEventListener('click', function() {
            if (walletConnected) {
                disconnectWallet();
            } else {
                openWalletModal();
            }
        });
    }
}

function openWalletModal() {
    if (walletModal) {
        walletModal.classList.add('active');
    }
}

function closeWalletModal() {
    if (walletModal) {
        walletModal.classList.remove('active');
    }
}

function connectWallet(walletType) {
    console.log(`Connecting to ${walletType} wallet...`);
    
    // Simulate wallet connection
    setTimeout(() => {
        walletConnected = true;
        walletBtn.innerHTML = '<i class="fas fa-wallet"></i><span>Connected</span>';
        walletBtn.classList.add('connected');
        closeWalletModal();
        
        console.log('✅ Wallet connected successfully!');
    }, 1000);
}

function disconnectWallet() {
    walletConnected = false;
    walletBtn.innerHTML = '<i class="fas fa-wallet"></i><span>接続</span>';
    walletBtn.classList.remove('connected');
    
    console.log('🔌 Wallet disconnected');
}

// Animation functionality
function initializeAnimations() {
    // Add glitch effect to hero title
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        heroTitle.setAttribute('data-text', heroTitle.textContent);
    }
    
    // Add scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.stat-card, .feature, .nft-card');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

// Utility functions
function scrollToSection(sectionId) {
    const section = document.querySelector(`#${sectionId}`);
    if (section) {
        section.scrollIntoView({
            behavior: 'smooth'
        });
    }
}

// Add fadeIn animation
const fadeInStyle = document.createElement('style');
fadeInStyle.textContent = `
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(fadeInStyle);

// Error handling
window.addEventListener('error', function(e) {
    console.error('Website error:', e.error);
});

// Performance monitoring
window.addEventListener('load', function() {
    console.log('🎯 Website loaded successfully!');
    console.log('📊 Performance metrics available');
});

// Export functions for global access
window.scrollToSection = scrollToSection;
window.connectWallet = connectWallet;
window.closeWalletModal = closeWalletModal; 