from django.contrib import admin
from .models import (
    Treatment, TreatmentFAQ, BeforeAfterImage, 
    TeamMember, Testimonial, BlogPost, Contact
)

class TreatmentFAQInline(admin.TabularInline):
    model = TreatmentFAQ
    extra = 1

class BeforeAfterImageInline(admin.TabularInline):
    model = BeforeAfterImage
    extra = 1

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_range', 'duration', 'featured')
    list_filter = ('category', 'featured')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [TreatmentFAQInline, BeforeAfterImageInline]

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'role', 'bio')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'treatment', 'date', 'featured')
    list_filter = ('featured', 'treatment')
    search_fields = ('name', 'quote')
    date_hierarchy = 'date'

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'responded')
    list_filter = ('responded', 'created_at')
    search_fields = ('name', 'email', 'message')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
