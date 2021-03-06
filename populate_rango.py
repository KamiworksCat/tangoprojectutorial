import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_django.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
    python_cat = add_cat('Python', views=128, likes=64)

    add_page(
        cat=python_cat,
        title="Official Python tutorial",
        url="http://docs.python.org/2/tutorial/"
    )

    add_page(
        cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteepress.com/thinkpython/"
    )

    add_page(
        cat=python_cat,
        title="Learn Python in 10 minutes",
        url="http://www.korokithakis.net/tutorials/python/"
    )

    django_cat = add_cat("Django", views=64, likes=32)

    add_page(
        cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/"
    )

    add_page(
        cat=django_cat,
        title="How to tango with Django",
        url="http://www.tangowithdjango.com/"
    )

    frame_cat = add_cat("Other Frameworks", views=32, likes=16)

    add_page(
        cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/"
    )

    add_page(
        cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org"
    )

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    return c

# Start execution here
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()