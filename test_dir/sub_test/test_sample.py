import seldom

class BingTest(seldom.TestCase):
    """
    selector find element
    """

    def test_bing_search(self):
        """
        A simple test
        """
        self.open("https://cn.bing.com/")
        self.type("#sb_form_q", text="seldom")
        self.click("tag=svg")
        self.assertInTitle("必应")
