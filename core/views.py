import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from core.models import News 

requests.packages.urllib3.disable_warnings()

def news_list(request):
	news_techcrunch = News.objects.all().filter(webpage="https://techcrunch.com/")[::-1]
	news_mashable = News.objects.all().filter(webpage="https://mashable.com/tech")[::-1]
	news_theverge = News.objects.all().filter(webpage="https://www.theverge.com/tech")[::-1]
	context = {
		'object_list_1': news_techcrunch,
        'object_list_2': news_mashable,
        'object_list_3': news_theverge,
	}
	return render(request, "home.html", context)

def scrape(request):
	session = requests.Session()
	
#https://techcrunch.com/    
	url = "https://techcrunch.com/"    
	content = session.get(url, verify=False).content
	soup = BSoup(content, "html.parser")
	NewsWeb = soup.find_all('div', {"class":"post-block post-block--image post-block--unread"})    
	#print(soup.prettify())    
	for artcile in NewsWeb:
		title = ""
		link = ""
		image = ""
		main = artcile.find_all('a')[0]
		title = main.text.strip()
		picture = artcile.find_all('img')[0]
		image = picture["src"]
		link = main['href']
		if (title != "" and link != ""):
		    new_reg = News()
		    new_reg.title = str(title)
		    new_reg.webpage = "https://techcrunch.com/"
		    new_reg.url = str(link.strip())
		    new_reg.image = str(image.strip())
		    new_reg.save()

#https://mashable.com/tech	
	url = "https://mashable.com/tech"    
	content = session.get(url, verify=False).content
	soup = BSoup(content, "html.parser")
	NewsWeb = soup.find_all('div', {"class":"flex flex-row overflow-x-auto space-x-8 overflow-y-hidden"})    
	#print(soup.prettify())    
	for artcile in NewsWeb:
		title = ""
		link = ""
		image = ""
		main = artcile.find_all('a')[0]
		link = ('https://mashable.com'+main['href'])
		main2 = main.find_all('img')[0]
		title = main2['alt']
		title = title.strip()
		picture = main2['src']
		image = picture.strip() 
		if (title != "" and link != ""):
		    new_reg = News()
		    new_reg.title = str(title)
		    new_reg.webpage = "https://mashable.com/tech"
		    new_reg.url = str(link.strip())
		    new_reg.image = str(image.strip())
		    new_reg.save()

#https://www.theverge.com/tech	
	url = "https://www.theverge.com/tech"    
	content = session.get(url, verify=False).content
	soup = BSoup(content, "html.parser")
	NewsWeb = soup.find_all('div', {"class":"c-entry-box--compact c-entry-box--compact--article"})    
	#print(soup.prettify())    
	for artcile in NewsWeb:
		title = ""
		link = ""
		image = ""
		main = artcile.find_all('a')[0]
		link = (main['href'])
		main2 = main.find_all('img')[0]
		picture = main2['src']
		image = "https://www.bairesdev.com/wp-content/uploads/2020/01/bairesdev-logo-blue.svg" #picture.strip()
		main = artcile.find_all('a')[1]
		title = main.text.strip()
		if (title != "" and link != ""):
		    new_reg = News()
		    new_reg.title = str(title)
		    new_reg.webpage = "https://www.theverge.com/tech"
		    new_reg.url = str(link.strip())
		    new_reg.image = str(image.strip())
		    new_reg.save()
    
	return redirect("../")
