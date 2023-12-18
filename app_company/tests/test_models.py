from django.test import TestCase

from app_company.models import Company
from app_company.tests.factories import CompanyFactory


class CompanyTestCase(TestCase):
    def test_str_should_return_company_name(self):
        company = CompanyFactory()

        self.assertEqual(str(company), company.name)
