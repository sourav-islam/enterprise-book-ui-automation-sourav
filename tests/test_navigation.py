import allure
from pages.home_page import HomePage
from pages.product_page import ProductPage

@allure.feature("Navigation System")
@allure.story("Validate Selected Book Item Redirection Paths")
@allure.severity(allure.severity_level.NORMAL)
def test_random_book_navigation(home_page: HomePage, product_page: ProductPage):
    """Validates that 5 randomly selected books open their correct details page."""
    with allure.step("Navigate to Homepage"):
        home_page.navigate()
    
    with allure.step("Select 5 Sample Index Entries from Catalog Grid"):
        random_indices = home_page.get_random_book_indices(count=5)
    
    for index in random_indices:
        with allure.step(f"Extract Meta Information for Catalog Book Index: {index}"):
            expected_data = home_page.get_book_data_by_index(index)
        
        with allure.step("Click Title Link and Redirect to Details View"):
            home_page.click_book_by_index(index)
        
        with allure.step("Assert Specification Profiles and Titles Match"):
            assert product_page.is_product_info_displayed(), "Product specifications are missing."
            assert product_page.get_product_title() == expected_data["title"]
        
        with allure.step("Return Back to Clean Homepage Directory Grid"):
            home_page.navigate()