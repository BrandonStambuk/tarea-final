from playwright.sync_api import Page, expect
import re
from time import sleep


class StatusPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_button = page.locator('button:has-text("Add")')
        self.name_input = page.locator('div[data-v-957b4417] input.oxd-input.oxd-input--active')
        self.save_button = page.locator('button:has-text("Save")')
        self.table_cards = 'div.oxd-table div.oxd-table-body div.oxd-table-card'
        
    def goto(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/employmentStatus")

    def add_status(self, name):
        self.add_button.click()
        self.page.wait_for_selector('input.oxd-input.oxd-input--active')  # Espera input visible
        self.name_input.fill(name)
        self.save_button.click()
        try:
            self.page.wait_for_selector('div.oxd-toast:has-text("Successfully Saved")', timeout=10000)
            return True
        except:
            return False    

    
    