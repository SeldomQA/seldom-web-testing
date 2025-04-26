import seldom
from selenium.webdriver import EdgeOptions


if __name__ == '__main__':
    edge_option = EdgeOptions()
    edge_option.add_argument("--headless=new")
    browser = {
        "browser": "edge",
        "options": edge_option
    }
    seldom.main(
        path="./test_dir",
        browser=browser,  # edge
        rerun=3,
        open=False
    )
