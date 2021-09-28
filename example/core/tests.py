from django.test import TestCase

from example.core.models import Author


class AuthorTests(TestCase):
    databases = ["default", "replica"]

    def test_create(self):
        Author.objects.create()
