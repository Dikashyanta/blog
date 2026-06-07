from .models import category
from about.models import social_links as SocialLinks

def get_categories(request):
    categories = category.objects.all()
    return dict(categories=categories)

def get_social_links(request):
    social_links = SocialLinks.objects.all()
    return dict(social_links=social_links)

