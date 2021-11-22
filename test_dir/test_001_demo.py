import seldom
from pages.sahitest_page import SahiPage


class LinkTest(seldom.TestCase):

    def start(self):
        self.open("https://sahitest.com/demo/")
        self.sahi = SahiPage(self.driver)

    def test_link(self):
        self.sahi.link_text.click()


class IFramesTest(seldom.TestCase):

    def start(self):
        self.open("https://sahitest.com/demo/iframesTest.htm")
        self.sahi = SahiPage(self.driver)

    def test_input(self):
        self.sahi.input_text.clear()
        self.sahi.input_text.send_keys("22222")
        self.sahi.input_button.click()
