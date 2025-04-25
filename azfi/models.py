from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Treatment(models.Model):
    CATEGORY_CHOICES = [
        ('FACE', 'Face'),
        ('BODY', 'Body'),
        ('INJECTABLES', 'Injectables'),
    ]
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    what_to_expect = models.TextField()
    price_range = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    image = models.ImageField(upload_to='treatments/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('treatment_detail', kwargs={'slug': self.slug})

class TreatmentFAQ(models.Model):
    treatment = models.ForeignKey(Treatment, related_name='faqs', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return f"{self.treatment.name} - {self.question}"

class BeforeAfterImage(models.Model):
    treatment = models.ForeignKey(Treatment, related_name='before_after_images', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    before_image = models.ImageField(upload_to='before_after/before/')
    after_image = models.ImageField(upload_to='before_after/after/')
    patient_age = models.PositiveIntegerField(null=True, blank=True)
    sessions = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.treatment.name} - {self.title}"

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/')
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return f"{self.name} - {self.role}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    treatment = models.ForeignKey(Treatment, blank=True, null=True, on_delete=models.SET_NULL, related_name='testimonials')
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    date = models.DateField(default=timezone.now)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Testimonial from {self.name}"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog/')
    excerpt = models.TextField(blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False, null=True, blank=True)
    
    class Meta:
        ordering = ['-published_date']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.name} ({self.created_at.strftime('%Y-%m-%d')})"
