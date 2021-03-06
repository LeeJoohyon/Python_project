from django.core.urlresolvers import resolve
from django.test import TestCase
from .views import home_page


class HomepageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
