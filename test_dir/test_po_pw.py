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
from pages.pw_page import BingPage
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect


class BingTest(seldom.TestCase):
    """
    page object 设计模式
    """
    def start(self):
        self.p = sync_playwright().start()
        self.chromium = self.p.chromium.launch(headless=False)
        self.page = self.chromium.new_page()

    def end(self):
        self.chromium.close()
        self.p.stop()

    def test_bing_search(self):
        """
        A simple test
        """
        self.page.goto("https://cn.bing.com/")
        bp = BingPage(self.page)
        bp.search_input.highlight()
        bp.search_input.fill("playwright")
        bp.search_icon.highlight()
        bp.search_icon.click()
        expect(self.page).to_have_title("playwright - 搜索")


if __name__ == '__main__':
    seldom.main()
