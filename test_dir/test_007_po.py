"""
page object model
Using the poium Library
https://github.com/SeldomQA/poium
```
> pip install poium
```
"""
import seldom
from seldom.utils import file
file.add_to_path(str(file.dir_dir))
from pages.po_page import BingPage


class BingTest(seldom.TestCase):
    """
    page object 设计模式
    """

    def test_bing_search(self):
        """
        A simple test
        """
        page = BingPage()
        page.open("https://cn.bing.com/")
        page.search_input.send_keys("seldom")
        page.search_button.click()
        self.assertInTitle("必应")


if __name__ == '__main__':
    seldom.main(browser='chrome', debug=True)
