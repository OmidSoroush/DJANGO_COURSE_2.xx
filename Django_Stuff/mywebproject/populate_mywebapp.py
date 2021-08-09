import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mywebproject.settings')

import django
# Import settings
django.setup()

import random
from mywebapp.models import Topic,Webpage,AccessRecord
from faker import Faker


fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t



def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        #get the topic for the entry
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic = top, url=fake_url, name = fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date=fake_date)



if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating completed')
