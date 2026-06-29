import allure
from pages.home_page import HomePage

@allure.feature("Homepage Capabilities")
@allure.story("Validate Layout and Core Structural Content")
@allure.severity(allure.severity_level.CRITICAL)
def test_homepage_validation(home_page: HomePage):
    """Verifies that the homepage loads successfully with required elements."""
    with allure.step("Navigate to the Target Homepage"):
        home_page.navigate()
    
    with allure.step("Verify Current URL and Page Title Match Expected"):
        assert home_page.get_url() == "https://books.toscrape.com/index.html"
        assert home_page.get_title() == "All products | Books to Scrape - Sandbox"
    
    with allure.step("Validate Visibility and Content of Structural Headings"):
        headings = home_page.get_all_headings()
        assert len(headings) > 0, "No visible headings found on the homepage."
        for heading in headings:
            assert heading != "", "Found a heading element with empty text."
        
    with allure.step("Verify Product Section Grid Component is Populated"):
        assert home_page.is_books_section_visible(), "Books container is not visible."
        assert home_page.get_book_count() > 0, "The books container exists but contains 0 items."