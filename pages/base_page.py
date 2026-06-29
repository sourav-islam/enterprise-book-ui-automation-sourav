from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://books.toscrape.com/index.html"

    def navigate(self, path: str = ""):
        """Navigates to a specific path or the base URL."""
        url = self.base_url if not path else f"https://books.toscrape.com/{path}"
        self.page.goto(url)

    def get_url(self) -> str:
        return self.page.url

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_selector(self, selector: str, timeout: float = 5000):
        """Dynamic wait mechanism to avoid hardcoded sleep periods."""
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)