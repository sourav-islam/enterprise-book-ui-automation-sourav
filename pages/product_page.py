from pages.base_page import BasePage
from playwright.sync_api import Page

class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.product_main_title = "div.product_main h1"
        self.product_price = "div.product_main p.price_color"
        self.product_stock_info = "div.product_main p.instock"

    def get_product_title(self) -> str:
        self.wait_for_selector(self.product_main_title)
        return self.page.locator(self.product_main_title).inner_text().strip()

    def get_product_price(self) -> str:
        return self.page.locator(self.product_price).inner_text().strip()

    def is_product_info_displayed(self) -> bool:
        return self.page.is_visible(self.product_stock_info)