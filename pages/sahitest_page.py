from poium import Page, Element


class SahiPage(Page):
    link_text = Element(link_text="Link Test", describe="Link Test")
    input_text = Element(id_="checkRecord", describe="input Text")
    input_button = Element(css="input[value='Click me']", describe="input button")

