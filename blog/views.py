from django.shortcuts import render

from blog.models import Arcticle


def home(request):
    articles = Arcticle.objects.all()
    context ={'arcticles': articles}
    return render(request, 'blog/Home.html', context)

def about(request):
    return render(request, 'blog/About.html')
