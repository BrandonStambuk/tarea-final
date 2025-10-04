from playwright.sync_api import Page

class PayGrade:
    def __init__(self, page: Page):
        self.page = page
        # Selectores generales de la tabla
        self.table_rows = ".oxd-table-body .oxd-table-row"
        self.name_column = "div[role='cell']:nth-child(2)"  # Columna "Name"
        self.currency_column = "div[role='cell']:nth-child(3)"  # Columna "Currency"
        self.delete_button = ".bi-trash"
        self.edit_button = ".bi-pencil-fill"

    def navigate(self, url: str):
        """Navega a la URL del módulo de Pay Grades"""
        self.page.goto(url)

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
        """Hace clic en el botón eliminar de la fila con el nombre dado"""
        row = self.page.locator(self.table_rows).filter(has_text=grade_name)
        row.locator(self.delete_button).click()

    def grade_exists(self, grade_name: str) -> bool:
        """Verifica si un grade existe en la tabla"""
        return self.page.locator(self.table_rows).filter(has_text=grade_name).count() > 0