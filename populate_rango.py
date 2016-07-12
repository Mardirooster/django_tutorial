import os
import django


def populate():
    python_cat = add_cat(name='Python',
        likes=128,
        views=64)

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/",
        likes=128,
        views=230)

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/",
        likes=136,
        views=10)

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/",
        likes=6,
        views=3)

    django_cat = add_cat(name="Django",
        likes=64,
        views=32)

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
        likes=4,
        views=2435)

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",
        likes=1,
        views=254)

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/",
        likes=32,
        views=432)

    frame_cat = add_cat(name="Other Frameworks",
        likes=32,
        views=16)

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",
        likes=53,
        views=233)

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org",
        likes=21,
        views=32)

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, likes=0, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, likes=likes, views=views)[0]
    return p

def add_cat(name,likes,views):
    c = Category.objects.get_or_create(name=name,likes=likes,views=views)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')
    django.setup()
    from rango.models import Category, Page
    populate()