from . models import CATEGORY
def menu_links(request):
    links = CATEGORY.objects.all()
    return dict(links=links)
