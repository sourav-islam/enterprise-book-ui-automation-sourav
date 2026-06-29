import allure
from pages.home_page import HomePage
from pages.product_page import ProductPage

@allure.feature("Data Validation Matrix")
@allure.story("Cross-Reference Item Consistency Across Views")
@allure.severity(allure.severity_level.CRITICAL)
def test_book_data_consistency(home_page: HomePage, product_page: ProductPage):
    """Validates that both Title and Price remain consistent between views."""
    with allure.step("Navigate to Homepage"):
        home_page.navigate()
    
    with allure.step("Select 5 Sample Index Entries from Catalog Grid"):
        random_indices = home_page.get_random_book_indices(count=5)
    
    for index in random_indices:
        with allure.step(f"Record Surface Grid Information for Index: {index}"):
            homepage_data = home_page.get_book_data_by_index(index)
            
        with allure.step("Click Book and Transition to Product Details Page"):
            home_page.click_book_by_index(index)
        
        with allure.step("Validate Deep Page Information Matches Surface Meta Data"):
            detail_title = product_page.get_product_title()
            detail_price = product_page.get_product_price()
            
            assert homepage_data["title"] == detail_title, "Data divergence observed in text titles."
            assert homepage_data["price"] == detail_price, "Price mismatch detected between views."
        
        with allure.step("Return Back to Homepage Grid"):
            home_page.navigate()