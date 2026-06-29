import pytest
from playwright.sync_api import sync_playwright, Page
from pages.home_page import HomePage
from pages.product_page import ProductPage

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def page(playwright_instance, request):
    # 1. Check if '--headed' was passed in the CLI command
    is_headless = not request.config.getoption("--headed", default=False)
    
    # 2. Check if '--slowmo' was passed in the CLI command
    slow_mo_val = request.config.getoption("--slowmo", default=0)

    # 3. Pass these dynamic variables into the launch configuration
    browser = playwright_instance.chromium.launch(headless=is_headless, slow_mo=slow_mo_val)
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture(scope="function")
def product_page(page: Page) -> ProductPage:
    return ProductPage(page)