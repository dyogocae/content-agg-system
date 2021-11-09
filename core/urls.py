from django.urls import path
from core.views import scrape, news_list

urlpatterns = [
	path('scrape/', scrape, name="scrape"),
	path('', news_list, name="home"),
]