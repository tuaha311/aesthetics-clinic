from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Treatment, TeamMember, Testimonial, BlogPost, BeforeAfterImage, Contact
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_treatments'] = Treatment.objects.filter(featured=True)[:3]
        context['testimonials'] = Testimonial.objects.filter(featured=True)[:3]
        context['team_members'] = TeamMember.objects.all()[:3]
        context['latest_posts'] = BlogPost.objects.all()[:3]
        return context

class TreatmentListView(ListView):
    model = Treatment
    template_name = 'treatments/treatment_list.html'
    context_object_name = 'treatments'
    
    def get_queryset(self):
        queryset = Treatment.objects.all()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Treatment.CATEGORY_CHOICES
        return context

class TreatmentDetailView(DetailView):
    model = Treatment
    template_name = 'treatments/treatment_detail.html'
    context_object_name = 'treatment'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        treatment = self.get_object()
        context['faqs'] = treatment.faqs.all()
        context['before_after'] = treatment.before_after_images.all()
        context['related_treatments'] = Treatment.objects.filter(
            category=treatment.category
        ).exclude(pk=treatment.pk)[:3]
        context['testimonials'] = treatment.testimonials.all()[:3]
        return context

class AboutView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = TeamMember.objects.all()
        return context

class GalleryView(ListView):
    model = BeforeAfterImage
    template_name = 'gallery.html'
    context_object_name = 'before_after_images'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = BeforeAfterImage.objects.select_related('treatment').all()
        category = self.request.GET.get('category')
        if category and category != 'all':
            queryset = queryset.filter(treatment__category__iexact=category)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Treatment.objects.values_list('category', flat=True).distinct()
        context['treatment_categories'] = Treatment.CATEGORY_CHOICES
        return context

class TestimonialListView(ListView):
    model = Testimonial
    template_name = 'testimonial_list.html'
    context_object_name = 'testimonials'

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add featured post
        try:
            context['featured_post'] = BlogPost.objects.filter(featured=True).latest('created_at')
        except (BlogPost.DoesNotExist, AttributeError):
            context['featured_post'] = None
            
        return context

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['recent_posts'] = BlogPost.objects.exclude(pk=post.pk)[:3]
        
        # Get next and previous posts
        try:
            context['next_post'] = BlogPost.objects.filter(created_at__gt=post.created_at).order_by('created_at').first()
        except BlogPost.DoesNotExist:
            context['next_post'] = None
            
        try:
            context['previous_post'] = BlogPost.objects.filter(created_at__lt=post.created_at).order_by('-created_at').first()
        except BlogPost.DoesNotExist:
            context['previous_post'] = None
            
        return context

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact_success')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your message has been sent successfully! We'll be in touch soon.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "There was an error with your submission. Please check the form and try again.")
        return super().form_invalid(form)

class ContactSuccessView(TemplateView):
    template_name = 'contact_success.html'

def search_view(request):
    query = request.GET.get('q', '')
    
    treatments = Treatment.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    ) if query else []
    
    posts = BlogPost.objects.filter(
        Q(title__icontains=query) | Q(content__icontains(query))
    ) if query else []
    
    context = {
        'query': query,
        'treatments': treatments,
        'posts': posts,
        'count': len(treatments) + len(posts)
    }
    
    return render(request, 'search_results.html', context)

def newsletter_signup(request):
    """Handle newsletter signups."""
    if request.method == 'POST':
        email = request.POST.get('email')
        # Here you would typically save the email to your database
        # or send it to your email marketing service
        
        # For now, just return a success message
        messages.success(request, "Thank you for subscribing to our newsletter!")
        
        # Redirect back to the referring page or home
        next_url = request.META.get('HTTP_REFERER', '/')
        return redirect(next_url)
    
    # If not a POST request, redirect to home
    return redirect('home')

def blog_search(request):
    """Search specifically within blog posts."""
    query = request.GET.get('q', '')
    
    posts = BlogPost.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) | Q(excerpt__icontains=query)
    ) if query else BlogPost.objects.all()[:6]
    
    context = {
        'posts': posts,
        'search_query': query,
    }
    
    return render(request, 'blog/blog_list.html', context)

def render_404(request, exception):
    return render(request, '404.html', status=404)