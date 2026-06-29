import pytest
import requests
import allure
from pages.home_page import HomePage



@allure.feature("Integrity Scanning")
@allure.story("Validate Surface Links Status Codes")
@allure.severity(allure.severity_level.NORMAL)
def test_broken_links_validation(home_page: HomePage):
    """Extracts all hyperlinks and screens them using HTTP requests."""
    with allure.step("Navigate to Homepage"):
        home_page.navigate()
        
    with allure.step("Collect and Deduplicate Catalog Hyperlinks"):
        unique_hrefs = home_page.get_all_hrefs()
    
    no_proxies = {"http": None, "https": None}
    
    for href in unique_hrefs:
        if href.startswith("index.html") or not href.startswith("http"):
            target_url = f"https://books.toscrape.com/{href.replace('index.html', '')}"
        else:
            target_url = href
            
        with allure.step(f"Verifying Link Status: {target_url}"):
            try:
                response = requests.head(target_url, timeout=10, verify=False, proxies=no_proxies)
                if response.status_code == 405:
                    response = requests.get(target_url, timeout=10, verify=False, proxies=no_proxies)
            except requests.RequestException as e:
                pytest.fail(f"URL connection failure for target {target_url}: {e}")
                
            assert response.status_code == 200, f"Broken link caught! {target_url} returned status {response.status_code}"