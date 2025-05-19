
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from datetime import datetime, timedelta
import traceback

caps = {
    "platformName": "Android",
    "platformVersion": "15",
    "deviceName": "2B291JEG80552",
    "appPackage": "io.ionic.vetez",
    "appActivity": "io.ionic.vetez.MainActivity",
    "automationName": "UiAutomator2",
    "noReset": True
}

options = UiAutomator2Options().load_capabilities(caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 15)

def safe_find(by, locator):
    return wait.until(EC.presence_of_element_located((by, locator)))

try:
    register_button = safe_find(By.ACCESSIBILITY_ID, "Register")
    register_button.click()

    # Use wait for each field instead of direct find_element
    first_name_field = safe_find(By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")
    last_name_field = safe_find(By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
    email_field = safe_find(By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText")
    dob_field = safe_find(By.XPATH, '//android.view.ViewGroup[@content-desc="BIRTHDATE"]/android.widget.TextView[2]')
    # dob_confirm_btn = driver.find_element(By.ID,"android:id/button1")
    phone_field = safe_find(By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.EditText")
    password_field = safe_find(By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.EditText")
    confirm_password_field = safe_find(By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.EditText")
    checkbox1 = safe_find(By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.widget.CheckBox[1]")
    checkbox2 = safe_find(By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.widget.CheckBox[2]")

    first_name = "John"
    last_name = "Doe"
    email = "sio.tetser022@gmail.com"
    phone = "545-373-2634"
    dob = "1994-02-02"
    password = "Aa123456!"

    def validate_email(email):
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

    def validate_dob(dob):
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        min_age_date = datetime.now() - timedelta(days=18*365)
        return dob_date <= min_age_date

    def validate_phone(phone):
        return re.match(r"^\d{3}-\d{3}-\d{4}$", phone)

    def validate_password(password):
        return re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$", password)

    if first_name and last_name:
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        last_name_field.clear()
        last_name_field.send_keys(last_name)
    else:
        print("Invalid name input.")

    if validate_email(email):
        email_field.clear()
        email_field.send_keys(email)
    else:
        print("Invalid email format.")

    if validate_dob(dob):
        dob_field.click()
        time.sleep(2)

        # year, month, day = map(int, dob.split("-"))
        # year_btn = safe_find(By.ID, "android:id/date_picker_header_year")
        # year_btn.click()
        # year_xpath = f'//android.widget.TextView[@text="{year}"]'
        # safe_find(By.XPATH, year_xpath).click()
        #
        # formatted_date = f"{day} {datetime(year, month, day).strftime('%b')} {year}"
        # date_xpath = f'//android.view.View[@content-desc="{formatted_date}"]'
        # safe_find(By.XPATH, date_xpath).click()

        # cancel_btn = wait.until(
        #     EC.element_to_be_clickable((By.ID, "android:id/button2"))
        # )
        # cancel_btn.click()
        #
        # time.sleep(2)

        dob_confirm_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "android:id/button1"))
        )
        dob_confirm_btn.click()
        time.sleep(2)
        # dob_confirm_btn.click()
    else:
        print("User must be at least 18 years old!")

    if validate_phone(phone):
        phone_field.clear()
        phone_field.send_keys(phone)
    else:
        print("Invalid phone number format!")

    if validate_password(password):
        password_field.clear()
        password_field.send_keys(password)
        confirm_password_field.clear()
        confirm_password_field.send_keys(password)
    else:
        print("Password does not meet strength requirements!")

    if not checkbox1.is_selected():
        checkbox1.click()
    if not checkbox2.is_selected():
        checkbox2.click()

    # Optional submit button click if needed
    register_submit_button = safe_find(By.ACCESSIBILITY_ID, "REGISTER NOW")
    register_submit_button.click()


except Exception as e:
    print("[!] Exception occurred:", e)
    print(driver.page_source)
    traceback.print_exc()

finally:
    time.sleep(5)
    driver.quit()
