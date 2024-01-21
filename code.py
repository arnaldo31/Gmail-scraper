from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')  # Required for headless mode on certain platforms

# Set up Selenium WebDriver with Chrome
driver = webdriver.Chrome(options=chrome_options)

# Replace 'https://example.com' with your target URL
url = 'https://example.com'

# Navigate to the URL
driver.get(url)

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extract text from the first h1 tag
h1_text = soup.find('h1').text

# Print the extracted text
print(f'Text of the first h1 tag: {h1_text}')

# Close the WebDriver
driver.quit()
