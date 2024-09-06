import os
import random
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# Load environment variables from .env file
load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

class PlaywrightFlows:
    """A utility class for handling Playwright flows within E2E tests."""
    def __init__(self):
        # Attributes
        self.p = sync_playwright().start()
        self.browser = self.p.firefox.launch(headless=True)
        self.page = None
        self.isSuccessful = False

    # Destructor
    def destruct(self):
        self.browser.close()
        self.p.stop()

    # Method to generate a new page
    def generate_new_page(self):
        self.isSuccessful = False
        self.context = self.browser.new_context(ignore_https_errors=True, viewport={'width': 1920, 'height': 1080})
        self.context.set_default_timeout(8000)
        self.context.tracing.start(screenshots=True, snapshots=True)
        self.page = self.context.new_page()

    # Method to teardown the page
    def teardown(self):
        self.page.close()
        if not self.isSuccessful:
            random_name = str(random.randint(1000, 9999))
            self.context.tracing.stop(path=f'test-results/{random_name}.zip')
        self.context.close()

    # Method  for logging in used in save_payment and complete_payment methods
    def login(self , timeout: int = 10000 ):
        if email and password:
            self.page.fill('#email', email)
            if self.page.is_visible('#btnNext'):
                self.page.wait_for_selector('#btnNext', timeout=timeout)
                self.page.click('#btnNext')
            self.page.fill('#password', password)
            self.page.wait_for_selector('#btnLogin', timeout=timeout)
            self.page.click('#btnLogin')
        else:
            raise ValueError('EMAIL or PASSWORD environment variable is not set')

    # Method for complete payment flow
    def complete_payment(self, checkout_url: str,  timeout: int = 10000) -> bool:
        try:
            self.page.goto(checkout_url)
            self.login(timeout=timeout)
            try:
                self.page.wait_for_selector('#payment-submit-btn', timeout=timeout)
            except Exception:
                self.page.go_back(timeout=timeout)
                self.page.wait_for_selector('#payment-submit-btn', timeout=timeout)
            self.page.click('#payment-submit-btn')
            try:
                self.page.wait_for_url('https://example.com/returnUrl**', timeout=timeout)
            except Exception:
                self.page.reload()
                self.page.wait_for_url('https://example.com/returnUrl**', timeout=timeout)
            self.isSuccessful = True
            return True
        except Exception as error:
            print(f'Error completing payment: {error}')
            return False

    # Method for saving payment method
    def save_payment(self, url: str , timeout: int = 10000) -> bool:
        try:
            self.page.goto(url)
            self.login(timeout=timeout)
            try:
                self.page.wait_for_selector('#consentButton', timeout=timeout)
            except Exception :
                self.page.go_back(timeout=timeout)
                self.page.wait_for_selector('#consentButton', timeout=timeout)
            self.page.click('#consentButton')
            try:
                self.page.wait_for_url('https://example.com/returnUrl**', timeout=timeout)
            except Exception:
                self.page.reload()
                self.page.wait_for_url('https://example.com/returnUrl**', timeout=timeout)
            self.isSuccessful = True
            return True
        except Exception as error:
            print(f'Error saving payment method: {error}')
            self.page.screenshot(path='error_screenshot.png')
            return False

    # Method for completing Helios verification
    def complete_helios_verification(self, checkout_url: str , timeout: int = 10000) -> bool:
        try:
            self.page.goto(checkout_url)
            try:
                self.page.wait_for_url('https://www.sandbox.paypal.com/webapps/helios?action=verify&flow=3ds**', timeout=timeout)
            except Exception:
                self.page.reload(timeout=timeout)
                self.page.wait_for_url('https://www.sandbox.paypal.com/webapps/helios?action=verify&flow=3ds**', timeout=timeout)
            self.page.wait_for_load_state('networkidle', timeout=timeout)
            frame = self.page.frame_locator('iframe[name="threedsIframeV2"]').frame_locator('iframe')
            input_field = frame.get_by_placeholder(' Enter Code Here' )
            submit_button = frame.get_by_role('button', name='SUBMIT' )
            if input_field.is_visible():
                input_field.click()
                input_field.fill('1234')
            if submit_button.is_visible():
                submit_button.click()
            try:
                self.page.wait_for_url('https://example.com/returnUrl**', timeout=timeout)
            except Exception:
                self.page.reload()
                self.page.wait_for_url('https://example.com/returnUrl**', timeout=timeout)
            self.isSuccessful = True
            return True
        except Exception as error:
            self.page.screenshot(path='error_screenshot.png')
            print(f'Error completing payment: {error}')
            return False