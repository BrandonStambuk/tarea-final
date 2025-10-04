import pytest
from pages.paygrade import PayGrade

def test_list_paygrades(page_logged):
    paygrade = PayGrade(page_logged.page)
    paygrade.navigate()
    grades = paygrade.get_all_grades()
    assert len(grades) > 0

def test_delete_paygrade(page_logged):
    """Verifica que se puede eliminar un Pay Grade existente"""
    paygrade = PayGrade(page_logged.page)
    paygrade.navigate()

    if paygrade.grade_exists("Grade 3"):
        paygrade.delete_grade("Grade 3")
        page_logged.page.wait_for_timeout(1000)
        assert not paygrade.grade_exists("Grade 3")
    else:
        import pytest
        pytest.skip("Grade 3 no existe en la tabla, se omite la prueba")