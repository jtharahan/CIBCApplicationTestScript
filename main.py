from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# setup
s = Service("./Drivers/geckodriver")
driver = webdriver.Firefox(service=s)
driver.implicitly_wait(10)
driver.get("https://www.investorsedge.cibc.com/en/home.html")
wait = WebDriverWait(driver, 60)

# test close cookies
wait.until(EC.element_to_be_clickable((By.ID, "button-1543586364705")))
f = driver.find_element(By.ID, "button-1543586364705")
f.click()

# test other links
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "CIBC.com")))
f = driver.find_element(By.LINK_TEXT, "CIBC.com")
f.click()
time.sleep(5)
assert "Personal Banking and Financial Services" in driver.title
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "CIBC Websites")))
f = driver.find_element(By.LINK_TEXT, "CIBC Websites")
f.click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "CIBC Investor's Edge")))
f = driver.find_element(By.LINK_TEXT, "CIBC Investor's Edge")
f.click()

wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "FAQ")))
f = driver.find_element(By.LINK_TEXT, "FAQ")
f.click()
time.sleep(5)
assert "Frequently Asked Questions" in driver.title
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "CIBC Websites")))
f = driver.find_element(By.LINK_TEXT, "CIBC Websites")
f.click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "CIBC Investor's Edge")))
f = driver.find_element(By.LINK_TEXT, "CIBC Investor's Edge")
f.click()

# test accounts and investments page
wait.until(EC.element_to_be_clickable((By.ID, "AccountsandInvestments")))
f = driver.find_element(By.ID, "AccountsandInvestments")
f.click()
assert "Accounts and Investments" in driver.title
f = driver.find_element(By.XPATH, "//*[text()='RRSP']")
f.click()
f = driver.find_element(By.XPATH, "//*[text()='RESP']")
f.click()

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Investments']")))
f = driver.find_element(By.XPATH, "//*[text()='Investments']")
f.click()
f = driver.find_element(By.XPATH, "//*[text()='Stocks']")
f.click()
f = driver.find_element(By.XPATH, "//*[text()='Mutual Funds']")
f.click()
f = driver.find_element(By.XPATH, "//*[text()='GICs']")
f.click()

time.sleep(5)

# test tools and research
wait.until(EC.element_to_be_clickable((By.ID, "ToolsandResearch")))
f = driver.find_element(By.ID, "ToolsandResearch")
f.click()
assert "Tools and Research" in driver.title
driver.execute_script("window.scrollTo(0, 1000)")

time.sleep(5)

# test pricing page
wait.until(EC.element_to_be_clickable((By.ID, "Pricing")))
f = driver.find_element(By.ID, "Pricing")
f.click()
assert "Pricing" in driver.title

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Regular investor']")))
f = driver.find_element(By.XPATH, "//*[text()='Regular investor']")
f.click()
driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(5)

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Young investor']")))
f = driver.find_element(By.XPATH, "//*[text()='Young investor']")
f.click()
driver.execute_script("window.scrollTo(0, 1000)")

time.sleep(5)

# test learn page
wait.until(EC.element_to_be_clickable((By.ID, "Learn")))
f = driver.find_element(By.ID, "Learn")
f.click()
assert "Learn" in driver.title

driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(5)
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Load 4 more articles']")))
f = driver.find_element(By.XPATH, "//*[text()='Load 4 more articles']")
f.click()
time.sleep(5)

# test getting started page
time.sleep(5)
wait.until(EC.element_to_be_clickable((By.ID, "GettingStarted")))
f = driver.find_element(By.ID, "GettingStarted")
f.click()
assert "Getting Started" in driver.title

driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(5)
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Fund your account']")))
f = driver.find_element(By.XPATH, "//*[text()='Fund your account']")
f.click()
driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(5)

wait.until(EC.element_to_be_clickable((By.ID, "accordion-1652941585199-tabpanel-0")))
f = driver.find_element(By.ID, "accordion-1652941585199-tabpanel-0")
f.click()
time.sleep(5)


# test main page
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "CIBC Websites")))
f = driver.find_element(By.LINK_TEXT, "CIBC Websites")
f.click()

wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "CIBC Investor's Edge")))
f = driver.find_element(By.LINK_TEXT, "CIBC Investor's Edge")
f.click()

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Explore learning resources']")))
f = driver.find_element(By.LINK_TEXT, "Explore learning resources")
f.click()
assert "Learning Resources" in driver.title

time.sleep(5)

# test contact us page
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact Us")))
f = driver.find_element(By.LINK_TEXT, "Contact Us")
f.click()
assert "Contact Us" in driver.title

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Chat']")))
f = driver.find_element(By.XPATH, "//*[text()='Chat']")
f.click()
driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(5)

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Email us']")))
f = driver.find_element(By.XPATH, "//*[text()='Email us']")
f.click()
driver.execute_script("window.scrollTo(0, 1000)")

time.sleep(5)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "accordionTitle")))
f = driver.find_element(By.CLASS_NAME, "accordionTitle")
f.click()

time.sleep(5)

# test sign on page
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "direct-signon-link")))
f = driver.find_element(By.CLASS_NAME, "direct-signon-link")
f.click()

wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "CIBC Investor's Edge")))
f = driver.find_element(By.LINK_TEXT, "CIBC Investor's Edge")
f.click()

time.sleep(5)

# exit
driver.close()
driver.quit()
print("Completed Test")



