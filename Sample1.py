import content
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the main page
driver.get("https://ps.demofms.com/Login.aspx")

# List of links to open
links = ["//*[@class="pdf-link blink]"]

# Open each link in a new tab
for link in links:
    driver.execute_script(f"window.open('{link}', '_blank');")
    time.sleep(1)  # Optional: small delay between opening tabs

# Switch between tabs
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    print(driver.title)  # Print the title of the current tab

# Close the browser
driver.quit()
