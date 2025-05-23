import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import re
import time
from appium.webdriver.common.appiumby import AppiumBy as By



import traceback
# -------- Pytest fixture to set up and tear down the driver --------
@pytest.fixture(scope="function")
def driver():
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
    yield driver
    driver.quit()

# -------- Helper to wait for element --------
def safe_find(driver, by, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))


def test_required_fields_validation(driver):
    # Navigate to Register screen
    safe_find(driver, By.ACCESSIBILITY_ID, "Register").click()

    # Try clicking REGISTER NOW by accessibility id first
    try:
        safe_find(driver, By.ACCESSIBILITY_ID, "REGISTER NOW").click()
    except Exception:
        # If not found, scroll to and click by visible text
        driver.find_element(By.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().text("REGISTER NOW"))').click()

    # Validate error messages for required fields
    assert safe_find(driver, By.XPATH, '//android.widget.TextView[@text="First name is required"]')
    assert safe_find(driver, By.XPATH, '//android.widget.TextView[@text="Last name is required"]')
    assert safe_find(driver, By.XPATH, '//android.widget.TextView[@text="Email is required"]')
    assert safe_find(driver, By.XPATH, '//android.widget.TextView[@text="Birthdate is required."]')
    assert safe_find(driver, By.XPATH, '//android.widget.TextView[@text="Phone number is required."]')
    assert safe_find(driver, By.XPATH, '//android.widget.TextView[@text="Password is required."]')
    assert safe_find(driver, By.XPATH, '//android.widget.TextView[@text="Confirm Password is required."]')
    assert safe_find(driver, By.XPATH, '//android.widget.TextView[@text="You need to agree to the terms and conditions."]')
    assert safe_find(driver, By.XPATH, '//android.widget.TextView[@text="You need to agree to receive mails regarding updates."]')

# -------- The actual test for required field validation --------


def test_first_name_validation(driver):

    #open register screen
    #safe_find(driver, By.ACCESSIBILITY_ID, "Register").click()  #use this line when run this case Individually
    #time.sleep(1)#use this line when run this case Individually

    # Locate the first name field (adjust XPath if needed)
    first_name_field = safe_find(driver, By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")

    # Invalid inputs to test
    invalid_names = ["     ", "123456", "@@!!"]
    for name in invalid_names:
        first_name_field.clear()
        first_name_field.send_keys(name)
        time.sleep(1)  # allow app to show real-time warning

        # Check for live warning message
        try:
            error = safe_find(driver, By.XPATH, '//android.widget.TextView[@text="Letters, spaces, periods only"]')
            assert error is not None
            print(f"✅ Test passed: '{name}' correctly triggered the warning.")
        except:
            print(f"❌ Test failed: '{name}' did not trigger the expected warning.")

def test_first_name_length_validation(driver):
    # Go to the Register screen

    #safe_find(driver, By.ACCESSIBILITY_ID, "Register").click()  #use this line when run this case Individually
   # time.sleep(1)  #use this line when run this case Individually

    # Locate the first name field (adjust XPath if needed)
    first_name_field = safe_find(driver, By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")

    # Invalid inputs to test
    invalid_names = ["a"]
    for name in invalid_names:
        first_name_field.clear()
        first_name_field.send_keys(name)
        time.sleep(1)  # allow app to show real-time warning

        # Check for live warning message
        try:
            error = safe_find(driver, By.XPATH, '//android.widget.TextView[@text="Too Short!"]')
            assert error is not None
            print(f"✅ Test passed: '{name}' correctly triggered the warning.")
        except:
            print(f"❌ Test failed: '{name}' did not trigger the expected warning.")



def test_last_name_validation(driver):
    # Go to the Register screen
    #safe_find(driver, By.ACCESSIBILITY_ID, "Register").click()  #use this line when run this case Individually
    #time.sleep(1)  #use this line when run this case Individually

    # Locate the first name field (adjust XPath if needed)
    last_name_field = safe_find(driver, By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")

    # Invalid inputs to test
    invalid_names = ["     ", "123456", "@@!!"]
    for name in invalid_names:
        last_name_field.clear()
        last_name_field.send_keys(name)
        time.sleep(1)  # allow app to show real-time warning

        # Check for live warning message
        try:
            error = safe_find(driver, By.XPATH, '//android.widget.TextView[@text="Letters, spaces, periods only"]')
            assert error is not None
            print(f"✅ Test passed: '{name}' correctly triggered the warning.")
        except:
            print(f"❌ Test failed: '{name}' did not trigger the expected warning.")


def test_last_name_length_validation(driver):
    # Go to the Register screen
    #safe_find(driver, By.ACCESSIBILITY_ID, "Register").click()      #use this line when run this case Individually
    #time.sleep(1)   #use this line when run this case Individually

    # Locate the first name field (adjust XPath if needed)
    last_name_field = safe_find(driver, By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")

    # Invalid inputs to test
    invalid_names = ["a"]
    for name in invalid_names:
        last_name_field.clear()
        last_name_field.send_keys(name)
        time.sleep(1)  # allow app to show real-time warning

        # Check for live warning message
        try:
            error = safe_find(driver, By.XPATH, '//android.widget.TextView[@text="Too Short!"]')
            assert error is not None
            print(f"✅ Test passed: '{name}' correctly triggered the warning.")
        except:
            print(f"❌ Test failed: '{name}' did not trigger the expected warning.")





def test_email_formate_validation(driver):
    #safe_find(driver, By.ACCESSIBILITY_ID, "Register").click()        #use this line when run this case Individually
    #time.sleep(1)  # Give the UI time to load        #use this line when run this case Individually

    # Locate the email field
    email_field = safe_find(driver, By.XPATH,
                            "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText")

    # Input an invalid email
    invalid_email = "invalid-email.com"
    email_field.clear()
    email_field.send_keys(invalid_email)

    # Submit the form
   # safe_find(driver, By.ACCESSIBILITY_ID, "REGISTER NOW").click()


    # Wait for the error message to appear
    time.sleep(1)

    # Check for the "Invalid Email Address" warning
    try:
        error_msg = safe_find(driver, By.XPATH, '//android.widget.TextView[@text="Invalid email format"]')
        assert error_msg is not None
        print("Test passed: Invalid email warning displayed.")
    except:
        print("Test failed: No invalid email warning found.")
import time
from appium.webdriver.common.appiumby import AppiumBy as By

def test_us_phone_number_format(driver):
    # Locate the phone number field (update XPath if needed)
    phone_field = safe_find(driver, By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.EditText")

    # Test inputs and expected result
    test_inputs = {
        "455-474-3723": False,  # ✅ valid, no error expected

        "455-474-372": True,    # ❌ too short

    }

    for phone, expect_error in test_inputs.items():
        print(f"\n🔎 Testing phone input: '{phone}'")

        phone_field.clear()
        phone_field.send_keys(phone)
        time.sleep(1)

        error_elements = driver.find_elements(By.XPATH, '//android.widget.TextView[@text="Phone number is not valid."]')

        if expect_error:
            if error_elements:
                print(f"✅ Test passed: Warning shown for invalid input '{phone}'")
            else:
                print(f"❌ Test failed: No warning for invalid input '{phone}'")
        else:
            if not error_elements:
                print(f"✅ Test passed: No warning shown for valid input '{phone}'")
            else:
                print(f"❌ Test failed: Warning incorrectly shown for valid input '{phone}'")




def test_password_validation(driver):
    # Locate the password field (adjust XPath or ID as needed)
    password_field = safe_find(driver, By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.EditText")

    # Invalid password inputs (one missing condition per case)
    test_cases = {
        "Ab1@": "Minimum length for Password is 8 character",  # Too short
        "abcdefgh": "Must use upper case, lower case, number and symbol",  # No upper, digit, symbol
        "ABCDEFGH": "Must use upper case, lower case, number and symbol",  # No lower, digit, symbol
        "abcd1234": "Must use upper case, lower case, number and symbol",  # No upper, symbol
        "ABCD1234": "Must use upper case, lower case, number and symbol",  # No lower, symbol
        "Abcd1234": "Must use upper case, lower case, number and symbol",  # No symbol
        "Abcd@123": None  # ✅ Valid password, should NOT show any warning
    }
    for pwd, expected_warning in test_cases.items():
        print(f"\n🔎 Testing password: '{pwd}'")

        password_field.clear()
        password_field.send_keys(pwd)
        time.sleep(1)

        if expected_warning:
            try:
                warning_element = safe_find(driver, By.XPATH, f'//android.widget.TextView[@text="{expected_warning}"]')
                assert warning_element is not None
                print(f"✅ Test passed: Warning '{expected_warning}' shown for '{pwd}'.")
            except:
                print(f"❌ Test failed: Expected warning '{expected_warning}' not shown for '{pwd}'.")
        else:
            # For valid password: make sure no warning appears
            warning1 = driver.find_elements(By.XPATH,
                                            '//android.widget.TextView[@text="Password is required."]')
            warning2 = driver.find_elements(By.XPATH,
                                            '//android.widget.TextView[@text="Must use uppercase, lowercase, number & symbol."]')

            if not warning1 and not warning2:
                print(f"✅ Test passed: '{pwd}' accepted as valid (no warnings shown).")
            else:
                print(f"❌ Test failed: '{pwd}' incorrectly triggered a warning.")


def test_password_visibility_toggle(driver):
    # Locate the password field
    password_field = safe_find(driver, By.XPATH,
                               "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.EditText")

    # Enter a password
    test_password = "Abcd@123"
    password_field.clear()
    password_field.send_keys(test_password)

    # Locate the "eye" icon (password visibility toggle button)
    eye_icon = safe_find(driver, By.XPATH,
                         '(//android.widget.TextView[@text=""])[1]')  # Adjust if needed

    # Step 1: Password should initially be hidden
    is_password_hidden = password_field.get_attribute("password") == "true"
    assert is_password_hidden, "❌ Test failed: Password should be hidden by default"
    print("✅ Password is hidden by default")

    # Step 2: Tap the eye icon to show the password
    eye_icon.click()
    time.sleep(1)

    is_password_visible = password_field.get_attribute("password") == "false"
    assert is_password_visible, "❌ Test failed: Password should be visible after tapping eye icon"
    print("✅ Password visibility toggled ON (plaintext shown)")

    # Step 3: Tap again to hide the password
    eye_icon.click()
    time.sleep(1)

    is_password_hidden_again = password_field.get_attribute("password") == "true"
    assert is_password_hidden_again, "❌ Test failed: Password should be hidden after tapping eye icon again"
    print("✅ Password visibility toggled OFF (hidden again)")




def test_confirm_password_visibility_toggle(driver):
    # Go to Register screen (uncomment when running standalone)
    # safe_find(driver, By.ACCESSIBILITY_ID, "Register").click()
    # time.sleep(1)

    # Locate the confirm password field
    confirm_password_field = safe_find(driver, By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.EditText")

    # Input test password
    test_confirm_password = "Abcd@123"
    confirm_password_field.clear()
    confirm_password_field.send_keys(test_confirm_password)

    # Locate the visibility toggle (eye icon)
    eye_icon = safe_find(driver, By.XPATH, '(//android.widget.TextView[@text=""])[2]')  # Adjust if needed

    # Step 1: Confirm password should be hidden initially
    is_password_hidden = confirm_password_field.get_attribute("password") == "true"
    assert is_password_hidden, "❌ Test failed: Confirm password should be hidden by default"
    print("✅ Confirm password is hidden by default")

    # Step 2: Tap eye icon to show password
    eye_icon.click()
    time.sleep(1)
    is_password_visible = confirm_password_field.get_attribute("password") == "false"
    assert is_password_visible, "❌ Test failed: Confirm password should be visible after tapping eye icon"
    print("✅ Confirm password visibility toggled ON (plaintext shown)")

    # Step 3: Tap eye icon again to hide password
    eye_icon.click()
    time.sleep(1)
    is_password_hidden_again = confirm_password_field.get_attribute("password") == "true"
    assert is_password_hidden_again, "❌ Test failed: Confirm password should be hidden after tapping eye icon again"
    print("✅ Confirm password visibility toggled OFF (hidden again)")




def test_password_and_confirm_password_match(driver):
    # Navigate to Register screen (uncomment if needed)
    # safe_find(driver, By.ACCESSIBILITY_ID, "Register").click()
    # time.sleep(1)

    # Locate the password and confirm password fields
    password_field = safe_find(driver, By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.EditText")
    confirm_password_field = safe_find(driver, By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.EditText")

    # Step 1: Enter mismatched passwords
    password_field.clear()
    password_field.send_keys("Abcd@123")

    confirm_password_field.clear()
    confirm_password_field.send_keys("Wrong@123")
    time.sleep(1)

    try:
        error = safe_find(driver, By.XPATH, '//android.widget.TextView[@text="Password and Confirm Password do not match"]')
        assert error is not None
        print("✅ Test passed: Mismatch error shown correctly when passwords differ.")
    except:
        print("❌ Test failed: Mismatch error NOT shown when passwords differ.")

    # Step 2: Enter matching passwords
    confirm_password_field.clear()
    confirm_password_field.send_keys("Abcd@123")
    time.sleep(1)

    try:
        errors = driver.find_elements(By.XPATH, '//android.widget.TextView[@text="Password and Confirm Password do not match"]')
        assert len(errors) == 0
        print("✅ Test passed: No error shown when passwords match.")
    except:
        print("❌ Test failed: Error shown even though passwords match.")

def test_valid_registration(driver):
    # Navigate to Register screen
    #safe_find(driver, By.ACCESSIBILITY_ID, "Register").click()         #use this line when run this case Individually

    # Fill valid data in all fields - replace XPATHs as needed based on your app
    safe_find(driver, By.XPATH,
              "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText").send_keys(
        "John")
    safe_find(driver, By.XPATH,
              "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText").send_keys(
        "Brown")
    safe_find(driver, By.XPATH,
              "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText").send_keys(
        "sio.tester054gmail.com")

    # For date picker, click and confirm (you may need to customize based on your app's picker)
    dob_field = safe_find(driver, By.XPATH,
                          '//android.view.ViewGroup[@content-desc="BIRTHDATE"]/android.widget.TextView[2]')
    dob_field.click()
    # Wait for confirm button on date picker and click
    dob_confirm_btn = safe_find(driver, By.ID, "android:id/button1")
    dob_confirm_btn.click()

    safe_find(driver, By.XPATH,
              "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.EditText").send_keys(
        "123-456-7890")
    safe_find(driver, By.XPATH,
              "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.EditText").send_keys(
        "ValidPass123!")
    safe_find(driver, By.XPATH,
              "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.EditText").send_keys(
        "ValidPass123!")

    # Click checkboxes for terms and updates
    checkbox1 = safe_find(driver, By.XPATH,
                          "//android.widget.ScrollView/android.view.ViewGroup/android.widget.CheckBox[1]")
    if not checkbox1.is_selected():
        checkbox1.click()
    checkbox2 = safe_find(driver, By.XPATH,
                          "//android.widget.ScrollView/android.view.ViewGroup/android.widget.CheckBox[2]")
    if not checkbox2.is_selected():
        checkbox2.click()

    # Click REGISTER NOW button
    safe_find(driver, By.ACCESSIBILITY_ID, "REGISTER NOW").click()

    # Verify success message (adjust text/XPATH to your app's success message)
    success_msg = safe_find(driver, By.XPATH, '//android.widget.TextView[@text="My Profile"]')
    assert success_msg is not None

