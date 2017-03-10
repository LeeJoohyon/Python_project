from django.test import LiveServerTestCase

class BaseTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()