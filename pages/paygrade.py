from playwright.sync_api import Page

class PayGrade:
    def __init__(self, page: Page):
        self.page = page
    
        self.table_rows = ".oxd-table-body .oxd-table-row"
        self.name_column = "div[role='cell']:nth-child(2)"  
        self.currency_column = "div[role='cell']:nth-child(3)" 
        self.delete_button = ".bi-trash"
        self.edit_button = ".bi-pencil-fill"

    def navigate(self):
        """Navega al módulo de Pay Grades usando el sidebar"""
        self.page.click("span:has-text('Admin')")
        self.page.click("span.oxd-topbar-body-nav-tab-item:has-text('Job')")
        self.page.click("a[role='menuitem']:has-text('Pay Grades')")
        self.page.wait_for_selector(self.table_rows, timeout=5000)

    def get_all_grades(self):
        """Devuelve una lista de todas las filas con su nombre y moneda"""
        rows = self.page.query_selector_all(self.table_rows)
        grades = []
        for row in rows:
            name = row.query_selector(self.name_column).inner_text()
            currency = row.query_selector(self.currency_column).inner_text()
            grades.append({"name": name, "currency": currency})
        return grades

    def edit_grade(self, grade_name: str):
        """Hace clic en el botón editar de la fila con el nombre dado"""
        row = self.page.locator(self.table_rows).filter(has_text=grade_name)
        row.locator(self.edit_button).click()

    def delete_grade(self, grade_name: str):
       """Hace clic en el botón eliminar de la fila con el nombre dado y confirma"""
       row = self.page.locator(self.table_rows).filter(has_text=grade_name)
       row.locator(self.delete_button).click()
       self.page.wait_for_selector("div.orangehrm-modal-footer button:has-text('Yes, Delete')", timeout=5000)
       self.page.click("div.orangehrm-modal-footer button:has-text('Yes, Delete')")
       self.page.wait_for_timeout(2000)

    def grade_exists(self, grade_name: str) -> bool:
        """Verifica si un grade existe en la tabla"""
        return self.page.locator(self.table_rows).filter(has_text=grade_name).count() > 0
