import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

import random
from ap.models import User
import faker

fakegen = faker.Faker()



def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.first_name()
        fake_ln = fakegen.last_name()
        fake_email = fakegen.email()

        webg = User.objects.get_or_create(fm=fake_name, lm =fake_ln, email=fake_email)[0]

if __name__ == '__main__':
    print('asdsad')
    populate()
