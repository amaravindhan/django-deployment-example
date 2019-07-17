import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

#Fake Population script
import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fake_gen = Faker()
topics = ['Search', 'Social', 'MarketPlace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N = 5):
    for entry in range(N):
        top = add_topic()

        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

if __name__ == '__main__':
    print("Populating script!")
    populate(25)
    print("Populating Complete!")
