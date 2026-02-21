from .models import Students
from faker import Faker
import random
fake =Faker()


def faker_db(n=10)->None:
    try:
        for i in range(0,n):
            name  =  fake.name()
            age  = random.randint(30,40)
            email = fake.email()
            adress = fake.address()


            Students.objects.create(name =name ,
                                    age =age ,
                                    email =email ,
                                    adress =adress )
    except Exception as e:
        print(e)