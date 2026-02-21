from faker import Faker
from .models import Students
import random
fake = Faker()
def fake_db()->None:
    try:
        for i in range(0,10):
            name  = fake.name()
            age = random.randint(20,25)
            email = fake.email()
            adress = fake.address()
            
            Students.objects.create(    
                name  = name,
                age = age,
                email = email,
                adress = adress,
            )
    except Exception as e:
        print(e)






