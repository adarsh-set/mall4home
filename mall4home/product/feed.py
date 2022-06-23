from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import pro_store
from django.urls import reverse

class pro_feed(Feed):
    title = "mall4home"
    link = "/drcommands/"
    description = "Every product in on page"
    def items(self):
        a = pro_store.objects.all()[:5]
        return a
    def item_title(self,item):
        return item.p_name
    def item_description(self,item):
        return truncatewords(item.p_desc,30)
    def item_link(self):
        return reverse("homepage")
        
