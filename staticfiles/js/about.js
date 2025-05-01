// About Page JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Counter animation for stats
    animateCounters();
    
    // Initialize image lazy loading
    initLazyLoading();
    
    // Team member read more links without modals
    initReadMoreLinks();
    
    // Initialize AOS (Animate On Scroll) if available
    initAOS();
});

// Function to animate the counters in the stats section
function animateCounters() {
    const statNumbers = document.querySelectorAll('.stat-number');
    
    statNumbers.forEach(statNumber => {
        const target = parseInt(statNumber.textContent);
        const duration = 1500; // Animation duration in milliseconds
        const frameDuration = 1000 / 60; // 60fps
        const totalFrames = Math.round(duration / frameDuration);
        let frame = 0;
        const countTo = parseInt(target.toString().replace(/[^\d]/g, ''), 10);
        const counter = setInterval(() => {
            frame++;
            const progress = frame / totalFrames;
            const currentCount = Math.round(countTo * progress);
            
            // Check if the current count differs from target
            if (parseInt(statNumber.textContent.replace(/[^\d]/g, '')) !== currentCount) {
                statNumber.textContent = currentCount + (statNumber.textContent.includes('+') ? '+' : '');
            }
            
            // Check if we've reached the target
            if (frame === totalFrames) {
                clearInterval(counter);
                statNumber.textContent = target.toString(); // Ensure the final displayed value is exactly what was specified
            }
        }, frameDuration);
    });
}

// Function to initialize lazy loading for images
function initLazyLoading() {
    if ('loading' in HTMLImageElement.prototype) {
        const images = document.querySelectorAll('img');
        images.forEach(img => {
            if (!img.loading) {
                img.loading = 'lazy';
            }
        });
    } else {
        // Fallback for browsers that don't support loading attribute
        const script = document.createElement('script');
        script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.3.2/lazysizes.min.js';
        document.body.appendChild(script);
        
        const images = document.querySelectorAll('img');
        images.forEach(img => {
            img.classList.add('lazyload');
            const src = img.getAttribute('src');
            img.setAttribute('data-src', src);
            img.setAttribute('src', 'data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==');
        });
    }
}

// Function to initialize read more links for team members without modals
function initReadMoreLinks() {
    const readMoreLinks = document.querySelectorAll('.read-more:not([data-bs-toggle="modal"])');
    
    readMoreLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Find the team member parent element
            const teamMember = this.closest('.team-member');
            if (!teamMember) return;
            
            // Find the bio element
            const bio = teamMember.querySelector('.member-bio');
            if (!bio) return;
            
            // Toggle expanded class
            if (bio.classList.contains('expanded')) {
                // Collapse bio
                bio.classList.remove('expanded');
                bio.style.maxHeight = null;
                this.textContent = 'Read More';
            } else {
                // Expand bio
                bio.classList.add('expanded');
                bio.style.maxHeight = bio.scrollHeight + 'px';
                this.textContent = 'Read Less';
            }
        });
    });
}

// Function to initialize AOS (Animate On Scroll) if available
function initAOS() {
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true
        });
    }
}

// Optional: Add smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href');
        if (targetId === '#') return; // Skip if it's just "#"
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            e.preventDefault();
            
            window.scrollTo({
                top: targetElement.offsetTop - 100, // Offset for fixed header
                behavior: 'smooth'
            });
        }
    });
});

// Optional: Add hover effects for facility items
const facilityItems = document.querySelectorAll('.facility-item');
facilityItems.forEach(item => {
    item.addEventListener('mouseenter', function() {
        const overlay = this.querySelector('.facility-overlay');
        if (overlay) {
            overlay.style.height = '100%';
            overlay.style.background = 'rgba(0, 0, 0, 0.6)';
        }
    });
    
    item.addEventListener('mouseleave', function() {
        const overlay = this.querySelector('.facility-overlay');
        if (overlay) {
            overlay.style.height = '';
            overlay.style.background = '';
        }
    });
}); 