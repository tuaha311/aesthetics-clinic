// Treatments Page JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Get all category buttons and treatment items
    const categoryButtons = document.querySelectorAll('.category-btn');
    const treatmentItems = document.querySelectorAll('.treatment-item');
    
    // Add click event listeners to category buttons
    categoryButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            categoryButtons.forEach(btn => btn.classList.remove('active'));
            
            // Add active class to clicked button
            this.classList.add('active');
            
            const selectedCategory = this.getAttribute('data-category');
            
            // Show/hide treatment items based on selected category
            treatmentItems.forEach(item => {
                if (selectedCategory === 'all' || item.getAttribute('data-category') === selectedCategory) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
            
            // Smooth scroll to treatments section
            document.querySelector('.treatments-list').scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        });
    });
    
    // Initialize AOS (Animate On Scroll) if available
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out'
        });
    }
    
    // Treatment image lazy loading
    if ('loading' in HTMLImageElement.prototype) {
        const images = document.querySelectorAll('.treatment-image img');
        images.forEach(img => {
            img.loading = 'lazy';
        });
    }
    
    // Smooth scroll for "Learn More" links
    document.querySelectorAll('.btn-treatment').forEach(link => {
        link.addEventListener('click', function(e) {
            // Only if the link is on the same page
            if (this.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                const targetId = this.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
}); 