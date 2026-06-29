import random
from typing import List, Dict
from pages.base_page import BasePage
from playwright.sync_api import Page

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.headings_selector = "h1, h2, h3, h4, h5, h6"
        self.books_section = ".page_inner"
        self.book_items = "article.product_pod"
        self.book_title_link = "article.product_pod h3 a"
        self.book_price = "article.product_pod .price_color"
        self.all_links = "a"
        self.product_images = "article.product_pod .image_container img"
        self.next_button = "li.next a"

    def get_all_headings(self) -> List[str]:
        self.page.wait_for_selector(self.headings_selector)
        headings = self.page.locator(self.headings_selector).all_inner_texts()
        return [text.strip() for text in headings if text]

    def is_books_section_visible(self) -> bool:
        return self.page.is_visible(self.books_section)

    def get_book_count(self) -> int:
        return self.page.locator(self.book_items).count()

    def get_random_book_indices(self, count: int = 5) -> List[int]:
        """Collects all items and selects a distinct random subset."""
        total_books = self.get_book_count()
        return random.sample(range(total_books), min(count, total_books))

    def click_book_by_index(self, index: int):
        self.page.locator(self.book_title_link).nth(index).click()

    def get_book_data_by_index(self, index: int) -> Dict[str, str]:
        """Captures contextual item metadata from the cards."""
        title_element = self.page.locator(self.book_title_link).nth(index)
        title = title_element.get_attribute("title") or title_element.inner_text()
        price = self.page.locator(self.book_price).nth(index).inner_text()
        return {"title": title.strip(), "price": price.strip()}

    def get_all_hrefs(self) -> List[str]:
        links = self.page.locator(self.all_links).all()
        hrefs = [link.get_attribute("href") for link in links]
        return list(set([h for h in hrefs if h]))

    def click_next_page(self) -> bool:
        """Navigates pagination boundaries safely if a next indicator exists."""
        if self.page.is_visible(self.next_button):
            self.page.click(self.next_button)
            return True
        return False