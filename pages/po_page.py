from poium import Page, Element


class BingPage(Page):
    """baidu page"""
    search_input = Element(id_="sb_form_q")
    search_button = Element(tag="svg")

