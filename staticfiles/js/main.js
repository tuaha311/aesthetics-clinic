// DOM Ready
document.addEventListener("DOMContentLoaded", function() {
    // Initialize Back to Top Button
    initBackToTop();
    
    // Initialize Cookie Consent
    initCookieConsent();
    
    // Add Smooth Scrolling to all links
    initSmoothScroll();
});

// Back to Top Button
function initBackToTop() {
    const backToTopBtn = document.getElementById('back-to-top');
    
    if (backToTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
            }
        });
        
        backToTopBtn.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
}

// Cookie Consent
function initCookieConsent() {
    const cookieConsent = document.getElementById('cookie-consent');
    const acceptBtn = document.getElementById('cookie-accept');
    const declineBtn = document.getElementById('cookie-decline');
    
    if (cookieConsent && acceptBtn && declineBtn) {
        // Check if user has already made a choice
        if (!localStorage.getItem('cookieConsent')) {
            // Show cookie consent banner
            cookieConsent.style.display = 'block';
            
            // Accept cookies
            acceptBtn.addEventListener('click', function() {
                localStorage.setItem('cookieConsent', 'accepted');
                cookieConsent.style.display = 'none';
            });
            
            // Decline cookies
            declineBtn.addEventListener('click', function() {
                localStorage.setItem('cookieConsent', 'declined');
                cookieConsent.style.display = 'none';
            });
        }
    }
}

// Smooth Scrolling
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Testimonial Slider (if using vanilla JS)
// For a real project, you might want to use a library like Swiper or Slick
function initTestimonialSlider() {
    const testimonialItems = document.querySelectorAll('.testimonial-item');
    let currentIndex = 0;
    
    if (testimonialItems.length > 1) {
        // Hide all items except the first one
        testimonialItems.forEach((item, index) => {
            if (index !== 0) {
                item.style.display = 'none';
            }
        });
        
        // Auto-scroll through testimonials
        setInterval(() => {
            testimonialItems[currentIndex].style.display = 'none';
            currentIndex = (currentIndex + 1) % testimonialItems.length;
            testimonialItems[currentIndex].style.display = 'block';
        }, 5000);
    }
}

// Before-After Image Comparison (basic version)
// For a real project, you might want to use a specialized plugin
function initBeforeAfterSlider() {
    const sliders = document.querySelectorAll('.before-after-slider');
    
    sliders.forEach(slider => {
        const beforeImage = slider.querySelector('.before-image');
        const afterImage = slider.querySelector('.after-image');
        const sliderHandle = slider.querySelector('.slider-handle');
        
        if (beforeImage && afterImage && sliderHandle) {
            slider.addEventListener('mousemove', function(e) {
                const sliderWidth = slider.offsetWidth;
                const offsetX = e.pageX - slider.getBoundingClientRect().left;
                const percentage = (offsetX / sliderWidth) * 100;
                
                // Ensure percentage is between 0 and 100
                const clampedPercentage = Math.max(0, Math.min(100, percentage));
                
                // Update the width of the before image
                beforeImage.style.width = `${clampedPercentage}%`;
                sliderHandle.style.left = `${clampedPercentage}%`;
            });
        }
    });
}

// Form validation (basic example)
function validateForm(formId) {
    const form = document.getElementById(formId);
    
    if (form) {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('is-invalid');
                } else {
                    field.classList.remove('is-invalid');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    }
} 