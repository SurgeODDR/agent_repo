from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize the webdriver
driver = webdriver.Chrome(options=options)

# Open the target page
driver.get("https://www.tennisenpadelvlaanderen.be/dashboard/tornooien")

# Allow time for manual login
print("Please log in manually in the opened browser window, then press Enter here to continue...")
input()

print("Starting to poll the page every 2 seconds for any button/link containing 'bevestig'...")

def find_and_click_bevestig():
    try:
        # Try to find any element that contains "bevestig" in any form (case-insensitive)
        # This will match bevestig, bevestigen, bevestigd, etc.
        xpath = "//*[contains(translate(normalize-space(text()), 'BEVESTIG', 'bevestig'), 'bevestig')]"
        elements = driver.find_elements(By.XPATH, xpath)
        
        if not elements:
            print("No matching elements found. Refreshing page in 2 seconds...")
            return False
            
        # Try each matching element (in case there are multiple)
        for element in elements:
            try:
                # Get the text for logging
                element_text = element.text.strip()
                print(f"Found element with text: '{element_text}'. Attempting to click...")
                
                # Scroll the element into view
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(0.5)  # Small delay after scroll
                
                # Click the element
                element.click()
                
                # Wait a moment to verify the click had an effect
                time.sleep(1)
                
                # Try to find the same text again - if we can't find it, assume click was successful
                try:
                    driver.find_element(By.XPATH, f"//*[contains(text(), '{element_text}')]")
                    print("Button still present after click - trying next element if available...")
                except:
                    print("Button no longer present - click appears successful!")
                    return True
                    
            except StaleElementReferenceException:
                print("Element became stale, will retry...")
                continue
            except Exception as e:
                print(f"Error clicking element: {str(e)}, trying next if available...")
                continue
                
        return False
    except Exception as e:
        print(f"Error during search: {str(e)}")
        return False

success = False
while not success:
    try:
        success = find_and_click_bevestig()
        if not success:
            time.sleep(2)
            driver.refresh()
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        time.sleep(2)
        driver.refresh()

print("Successfully clicked the button! Closing browser in 3 seconds...")
time.sleep(3)
driver.quit()