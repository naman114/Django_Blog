from django.shortcuts import render

# List of dictionaries
posts = [
    {
        "author": "Naman Gogia",
        "title": "Blog Post 1",
        "content": "Blog Post 1 Content",
        "date_posted": "March 16, 2021",
    },
    {
        "author": "CoreyMS",
        "title": "Blog Post 2",
        "content": "Blog Post 2 Content",
        "date_posted": "March 17, 2021",
    },
]


# Function to handle traffic from our home. Returns what the user will see
def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


# data is passed to the template using context. From there, we can use posts key to access the list of dictionaries i.e. posts


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
