import random
import string
from django.shortcuts import render
from main.forms import UrlForm
from main.models import Urls
from django.urls import reverse
from django.shortcuts import redirect
from django.core import serializers



def home(request):
    breakpoint()
    all_urls = Urls.objects.all()

    return render(
            request, 
            'home_page.html', 
            context = {'all_urls': all_urls}
            )
def url_shorter(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url_from_html = form.cleaned_data['url']
            new_url = Urls.objects.create(
                    url = url_from_html, 
                    shorter_url=''.join(random.choice(string.ascii_letters)for x in range(9)))
            new_url.save()
            return reverse('main:home')
    else:
        form = Urls()
    return render(request, 'form.html')



def url_redirect(request, slug):
    return redirect(Urls.objects.get(shorter_url=slug).url)
