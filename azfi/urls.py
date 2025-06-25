from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('defaultsite', views.HomeView.as_view(), name='home_page'), #monkey patch for ionos default site to homepage
    
    # Treatments
    path('treatments/', views.TreatmentListView.as_view(), name='treatment_list'),
    path('treatments/<slug:slug>/', views.TreatmentDetailView.as_view(), name='treatment_detail'),
    
    # About
    path('about/', views.AboutView.as_view(), name='about'),
    
    # Gallery
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    
    # Testimonials
    path('testimonials/', views.TestimonialListView.as_view(), name='testimonial_list'),
    
    # Blog
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/search/', views.blog_search, name='blog_search'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    
    # Contact
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/success/', views.ContactSuccessView.as_view(), name='contact_success'),
    
    # Search
    path('search/', views.search_view, name='search'),
    
    # Newsletter Signup
    path('newsletter-signup/', views.newsletter_signup, name='newsletter_signup'),
] 

