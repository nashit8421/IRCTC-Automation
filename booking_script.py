import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
def open_irctc(driver, username, password):
    driver.get("https://www.irctc.co.in/nget/train-search")
    wait = WebDriverWait(driver, 20)

    # Login process
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'loginText')))
    login_button.click()
    username_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="userid"]')))
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="password"]')
    captcha_input = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="captcha"]')
    username_input.send_keys(username)
    password_input.send_keys(password)
    captcha_input.click()
    print("Solve the captcha and click login")

    # # Verify login
    # try:
    #     wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Logout')]")))
    #     print("Login successful.")
    # except TimeoutException:
    #     print("Login timeout. Please check the site for changes or ensure you have logged in.")
    # Verify login
    while True:
        if driver.find_element(By.XPATH, "//span[contains(text(), 'Logout')]").text != "":
            print("Login successful.")
            break


def input_station_details(driver, journey_date,source_station,destination_station):
    wait = WebDriverWait(driver, 10)
    
    # Enter source station name and select the first suggestion
    source_station_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[aria-autocomplete="list"].ng-tns-c57-8')))
    source_station_input.send_keys(source_station)
    # Wait for the autocomplete options to appear and select the first option
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ng-tns-c57-8[role="option"]'))).click()

    # Enter destination station name and select the first suggestion
    destination_station_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[aria-autocomplete="list"].ng-tns-c57-9')))
    destination_station_input.send_keys(destination_station)
    # Wait for the autocomplete options to appear and select the first option
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ng-tns-c57-9[role="option"]'))).click()

    # Enter the journey date
    date_input = wait.until(EC.visibility_of_element_located((By.ID, 'jDate')))
    ActionChains(driver).move_to_element(date_input).click(date_input).double_click().click_and_hold().send_keys(Keys.CLEAR).send_keys(journey_date).perform()
    # Select 'Tatkal' from the dropdown
    dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ng-tns-c65-12.ui-dropdown')))
    dropdown.click()
    tatkal_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='TATKAL']")))
    tatkal_option.click()

    # Click the 'Search' button
    search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.search_btn.train_Search')))
    search_button.click()



def wait_for_url(driver, target_url):
    WebDriverWait(driver, 300).until(EC.url_to_be(target_url))
    print(f"Page redirected to {target_url} successfully.")


def input_passenger_details(driver, passengers, infant_passengers):
    wait = WebDriverWait(driver, 20)  # Increased wait time
    add_passenger_link_xpath = "//a[.//span[contains(text(), '+ Add Passenger')]]"

    for index, (name, age, gender) in enumerate(passengers):
        if index > 0:  # Wait to add more passengers after the first
            add_passenger_btn = wait.until(EC.element_to_be_clickable((By.XPATH, add_passenger_link_xpath)))
            add_passenger_btn.click()
            time.sleep(2)  # Let the UI finish rendering

        # Handle the dynamic nature of input fields
        # Fetch all available name inputs and pick the one corresponding to this index
        name_inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[placeholder="Passenger Name"]')))
        age_inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[formcontrolname="passengerAge"]')))
        gender_dropdowns = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'select[formcontrolname="passengerGender"]')))

        # Check if the length of the lists is sufficient for the current index
        if len(name_inputs) <= index or len(age_inputs) <= index or len(gender_dropdowns) <= index:
            print(f"Error: Not enough input fields for passenger {index + 1}")
            continue

        name_inputs[index].send_keys(name)
        age_inputs[index].send_keys(str(age))
        gender_dropdowns[index].send_keys(gender)
    # Function to add an infant
    add_infant_link_text = "+ Add Infant Without Berth"
    for name, age, gender in infant_passengers:
        add_infant_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{add_infant_link_text}']")))
        add_infant_btn.click()
        time.sleep(2)  # Wait for the UI to respond

        infant_name_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="name"]')))
        infant_age_select = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[formcontrolname="age"]')))
        infant_gender_select = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[formcontrolname="gender"]')))

        infant_name_input.send_keys(name)
        infant_age_select.send_keys(str(age))
        infant_gender_select.send_keys(gender)

def finalize_booking_details(driver):
    wait = WebDriverWait(driver, 20)
    
    # Click on 'Consider for Auto Upgradation' checkbox
    auto_upgrade_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Consider for Auto Upgradation')]")))
    auto_upgrade_checkbox_id = auto_upgrade_label.get_attribute("for")
    auto_upgrade_checkbox = driver.find_element(By.ID, auto_upgrade_checkbox_id)
    if not auto_upgrade_checkbox.is_selected():
        driver.execute_script("arguments[0].click();", auto_upgrade_checkbox)

    # Click on 'Book only if confirm berths are allotted' checkbox
    confirm_berths_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Book only if confirm berths are allotted')]")))
    confirm_berths_checkbox_id = confirm_berths_label.get_attribute("for")
    confirm_berths_checkbox = driver.find_element(By.ID, confirm_berths_checkbox_id)
    if not confirm_berths_checkbox.is_selected():
        driver.execute_script("arguments[0].click();", confirm_berths_checkbox)
    # Click on radio button 'No, I don't want travel insurance'
    no_insurance_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 't want travel insurance')]")))
    no_insurance_radio_id = no_insurance_label.get_attribute("for")
    no_insurance_radio = driver.find_element(By.ID, no_insurance_radio_id)
    no_insurance_radio.click()

    # Click on radio button 'Pay through BHIM/UPI'
    upi_payment_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Pay through BHIM')]")))
    upi_payment_radio_id = upi_payment_label.get_attribute("for")
    upi_payment_radio = driver.find_element(By.ID, upi_payment_radio_id)
    upi_payment_radio.click()

    # Click on the 'Continue' button
    continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]")))
    continue_button.click()

    print("Final booking steps completed.")




if __name__ == "__main__":
    options = uc.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    driver = uc.Chrome(options=options)
    driver.maximize_window()
    # User credentials and journey date
    USERNAME = "USERNAME"
    PASSWORD = "PASSWORD"
    JOURNEY_DATE = "15/04/2024"  # User should replace 'dd/mm/yyyy' with the actual date
    source_station = "PUNE"
    destination_station = "AHMADNAGAR"
    open_irctc(driver, USERNAME, PASSWORD)
    input_station_details(driver, JOURNEY_DATE,source_station,destination_station)
    passengers = [('John Doe', 30, 'Male'), ('Jane Doe', 28, 'Female')]
    """
    Infant Ages : 
    Below one year
    One year
    Two years
    Three years
    Four years
    """
    infant_passengers = [("My Baby", "Below one year" , "Male")]
    wait_for_url(driver, "https://www.irctc.co.in/nget/booking/psgninput")
    input_passenger_details(driver, passengers,infant_passengers)
    finalize_booking_details(driver)