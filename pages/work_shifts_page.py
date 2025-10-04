from playwright.sync_api import Page


class WorkShiftPage:
    def __init__(self, page: Page):
        self.page = page

        self.admin_menu = "//span[text()='Admin']"
        self.job_menu = "//span[text()='Job ']"
        self.work_shift_menu = "//a[text()='Work Shifts']"

        self.add_button = "button.oxd-button--secondary"
        self.shift_name_input = "//label[text()='Shift Name']/following::input[1]"
        self.from_time_input = "//label[text()='From']/following::input[1]"
        self.to_time_input = "//label[text()='To']/following::input[1]"

        self.assign_employee_input = "//input[@placeholder='Type for hints...']"
        self.employee_dropdown_option = "//div[@role='option']"
        self.all_employees_checkbox = "//span[contains(text(),'All')]/preceding-sibling::span"

        self.save_button = "button[type='submit']"
        self.cancel_button = "//button[text()=' Cancel ']"

        self.shift_rows = "div.oxd-table-card"
        self.edit_button = "//i[@class='oxd-icon bi-pencil-fill']"
        self.delete_button = "//i[@class='oxd-icon bi-trash']"
        self.confirm_delete_button = "//button[text()=' Yes, Delete ']"

        self.success_message = "//p[text()='Successfully Saved']"
        self.error_message = "//span[contains(@class, 'oxd-input-field-error-message')]"

    def navigate_to_work_shifts(self):
        self.page.click(self.admin_menu)
        self.page.click(self.job_menu)
        self.page.click(self.work_shift_menu)

    def click_add_work_shift(self):
        self.page.click(self.add_button)

    def fill_work_shift_form(self, shift_name: str, from_time: str, to_time: str):
        self.page.fill(self.shift_name_input, shift_name)
        self.page.fill(self.from_time_input, from_time)
        self.page.fill(self.to_time_input, to_time)

    def assign_employee_to_shift(self, employee_name: str):
        self.page.fill(self.assign_employee_input, employee_name)
        self.page.wait_for_timeout(1000)
        self.page.click(self.employee_dropdown_option.first)

    def assign_all_employees(self):
        self.page.click(self.all_employees_checkbox)

    def save_work_shift(self):
        self.page.click(self.save_button)

    def cancel_work_shift(self):
        self.page.click(self.cancel_button)

    def is_success_message_visible(self) -> bool:
        return self.page.locator(self.success_message).is_visible()

    def search_work_shift(self, shift_name: str):
        search_input = self.page.locator("//label[text()='Shift Name']/following::input[1]")
        search_input.fill(shift_name)
        self.page.click("button[type='submit']")

    def edit_work_shift(self, old_shift_name: str, new_shift_name: str):
        self.search_work_shift(old_shift_name)
        self.page.click(self.edit_button.first)
        self.page.fill(self.shift_name_input, new_shift_name)
        self.page.click(self.save_button)

    def delete_work_shift(self, shift_name: str):
        self.search_work_shift(shift_name)
        self.page.click(self.delete_button.first)
        self.page.click(self.confirm_delete_button)

    def get_work_shifts_count(self) -> int:
        return self.page.locator(self.shift_rows).count()

    def is_work_shift_visible(self, shift_name: str) -> bool:
        shift_locator = self.page.locator(f"//div[text()='{shift_name}']")
        return shift_locator.is_visible()