from django.shortcuts import render
from .models import Post

# Function to handle traffic from our home. Returns what the user will see
def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


# data is passed to the template using context. From there, we can use posts key to access the list of dictionaries i.e. posts


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
