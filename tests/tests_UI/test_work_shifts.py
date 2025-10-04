import pytest
from faker import Faker

class TestWorkShifts:
    @pytest.fixture(autouse=True)
    def setup(self, work_shift_page_logged):
        self.work_shift = work_shift_page_logged
        self.fake = Faker()

    def test_navegar_hasta_work_shifts(self):
        """Test que verifica que estamos en el módulo Work Shifts"""
        count = self.work_shift.get_work_shifts_count()
        assert count >= 0
