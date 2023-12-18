from factory.django import DjangoModelFactory
from factory.faker import Faker

from app_company.models import Company


class CompanyFactory(DjangoModelFactory):
    name = Faker('company')
    description = Faker('text')

    class Meta:
        model = Company
