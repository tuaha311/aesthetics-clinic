from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Treatment, 
    TreatmentFAQ, 
    BeforeAfterImage, 
    TeamMember, 
    Testimonial, 
    BlogPost, 
    Contact
)

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_range', 'duration', 'featured', 'display_image')
    list_filter = ('category', 'featured', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
    
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.image.url)
        return "-"
    display_image.short_description = 'Image'

class TreatmentFAQInline(admin.TabularInline):
    model = TreatmentFAQ
    extra = 1

@admin.register(BeforeAfterImage)
class BeforeAfterImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'treatment', 'display_before_image', 'display_after_image', 'created_at')
    list_filter = ('treatment', 'created_at')
    search_fields = ('title', 'treatment__name')
    
    def display_before_image(self, obj):
        if obj.before_image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.before_image.url)
        return "-"
    display_before_image.short_description = 'Before'
    
    def display_after_image(self, obj):
        if obj.after_image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.after_image.url)
        return "-"
    display_after_image.short_description = 'After'

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'display_image', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'role', 'bio')
    
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />', obj.image.url)
        return "-"
    display_image.short_description = 'Photo'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'treatment', 'featured', 'date', 'display_image')
    list_filter = ('featured', 'date', 'treatment')
    search_fields = ('name', 'quote')
    list_editable = ('featured',)
    
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />', obj.image.url)
        return "-"
    display_image.short_description = 'Photo'

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'display_image')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    
    def display_image(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.featured_image.url)
        return "-"
    display_image.short_description = 'Featured Image'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'responded')
    list_filter = ('responded', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
    list_editable = ('responded',)
    
    def has_add_permission(self, request):
        return False  # Prevent adding contacts through admin

# Update Treatment admin to include FAQs inline
class TreatmentAdminWithFAQs(TreatmentAdmin):
    inlines = [TreatmentFAQInline]

# Re-register Treatment with inlines
admin.site.unregister(Treatment)
admin.site.register(Treatment, TreatmentAdminWithFAQs)

# Optional: Customize admin site header and title
admin.site.site_header = 'Aesthetics Clinic Administration'
admin.site.site_title = 'Aesthetics Clinic Admin'
admin.site.index_title = 'Clinic Management'
