import pytest
from pages.paygrade import PayGrade

def test_list_paygrades(page_logged):
    """Verifica que se listan los Pay Grades en la tabla"""
    paygrade = PayGrade(page_logged.page)
    paygrade.navigate("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewPayGrades")
    page_logged.page.wait_for_selector(paygrade.table_rows, timeout=5000)
    grades = paygrade.get_all_grades()
    assert len(grades) > 0, "No se encontraron Pay Grades en la tabla"
    assert any(g["name"] == "Grade 1" for g in grades)

def test_delete_paygrade(page_logged):
    """Verifica que se puede eliminar un Pay Grade existente"""
    paygrade = PayGrade(page_logged.page)
    paygrade.navigate("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewPayGrades")

    if paygrade.grade_exists("Grade 3"):
        paygrade.delete_grade("Grade 3")
        page_logged.page.wait_for_timeout(1000)
        assert not paygrade.grade_exists("Grade 3")
