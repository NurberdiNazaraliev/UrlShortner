from django.shortcuts import render, redirect
from .models import short_url
from .forms import UrlForm, ShortUrlForm
from .shortner import Shortener


# Create your views here.
def home(request):
    form = UrlForm(request.POST)
    a=""
    if request.method == "POST":
        if form.is_valid():
            NewUrl=form.save(commit=False)
            a=Shortener().issue_token()
            NewUrl.short_url=a
            NewUrl.save()
        else:
            form = UrlForm()
            a="invalid url"
    return render(request, 'shortner/home.html', {'form':form, 'a':a})


##def get_link(request, token):
    ##long_url=short_url.objects.filter(short_url=token)[0]
    ##return redirect (long_url.long_url)

def get_og_link(request):
    form = ShortUrlForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            short_url_req = form.cleaned_data['short_url']
            requested_url_obj = short_url.objects.get(short_url=short_url_req)
            return redirect(requested_url_obj.long_url)
    else:
        form = ShortUrlForm()
    return render(request, 'shortner/get_og_link.html', {'form':form})



