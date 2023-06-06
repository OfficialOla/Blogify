from django.shortcuts import render
from datetime import date

my_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Yinka Oniyide",
        "date": date(2023, 5, 28),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountain!."
                   "And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "contents": """
                    Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
                    when an unknown printer took a galley of type and scrambled it to make a type specimen book.
                    It has survived not only five centuries, but also the leap into electronic typesetting,
                    remaining essentially unchanged.
                    """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Yinka Oniyide",
        "date": date(2023, 2, 15),
        "title": "Programming Is Great",
        "excerpt": "Did you ever spend hours searching for tha error in your code?!",
        "contents": """
                    Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
                    when an unknown printer took a galley of type and scrambled it to make a type specimen book.
                    It has survived not only five centuries, but also the leap into electronic typesetting,
                    remaining essentially unchanged.
                    """
    },
    {
        "slug": "figma-designs",
        "image": "learningFigma.jpg",
        "author": "Yinka Oniyide",
        "date": date(2021, 10, 8),
        "title": "Introduction To UI/UX",
        "excerpt": "Every great Software Engineers out there must be design-centric!",
        "contents": """
                    Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
                    when an unknown printer took a galley of type and scrambled it to make a type specimen book.
                    It has survived not only five centuries, but also the leap into electronic typesetting,
                    remaining essentially unchanged.
                    """
    }
]


# Create your views here.
def landing_page(request):
    return render(request, "yo_blog/index.html")


def posts(request):
    return render(request, "yo_blog/all-posts.html")
    pass


def post_detail(request, slug):
    return render(request, "yo_blog/post-detail.html")
    pass
