from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_menu = "a[href='/web/index.php/admin/viewAdminModule']"
        self.job_menu = "span.oxd-topbar-body-nav-tab-item:has-text('Job')"
        self.job_titles_link = "a.oxd-topbar-body-nav-tab-link:has-text('Job Titles')"

    def go_to_admin(self):
        """Click en el menú lateral -> Admin"""
        self.page.locator(self.admin_menu).click()

    def open_job_dropdown(self):
        """Abrir el menú desplegable de Job"""
        self.page.locator(self.job_menu).click()

    def go_to_job_titles(self):
        """Seleccionar Job Titles del menú desplegable"""
        self.page.locator(self.job_titles_link).click()
