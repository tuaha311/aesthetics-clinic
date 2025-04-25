from django import template

register = template.Library()

@register.inclusion_tag('components/hero.html')
def hero(title="Our Gallery", subtitle="See the stunning results of our aesthetic treatments"):
    return {
        'title': title,
        'subtitle': subtitle
    }

@register.inclusion_tag('components/cta.html')
def cta():
    return
