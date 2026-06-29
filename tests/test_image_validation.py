import allure
from pages.home_page import HomePage

@allure.feature("Media System Validation")
@allure.story("Scan Paginated Grid Elements for Descriptive Requirements")
@allure.severity(allure.severity_level.MINOR)
def test_product_image_validation(home_page: HomePage):
    """Loops through pagination boundaries up to 5 pages validating catalog image attributes."""
    with allure.step("Navigate to Homepage Context"):
        home_page.navigate()
        
    max_pages = 5
    current_page = 1
    
    while current_page <= max_pages:
        images = home_page.page.locator(home_page.product_images).all()
        
        with allure.step(f"Validating {len(images)} Asset Thumbnails on Page {current_page}"):
            for img in images:
                assert img.is_visible()
                src = img.get_attribute("src")
                alt = img.get_attribute("alt")
                class_attr = img.get_attribute("class") or ""
                
                assert src and len(src.strip()) > 0, "Missing or blank 'src' image path attribute."
                assert alt and len(alt.strip()) > 0, "Missing structural accessibility 'alt' descriptive text."
                assert "thumbnail" in class_attr, f"Expected thumbnail CSS class structural sequence mismatch: {class_attr}"
            
        if current_page < max_pages and home_page.click_next_page():
            current_page += 1
        else:
            break