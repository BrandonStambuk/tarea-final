from pages.home_page import HomePage
from pages.job_titles_page import JobTitlesPage
from datetime import datetime
import json
import pytest

def load_job_data():
    with open("data/job_titles.json", "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.mark.parametrize("job", load_job_data())
def test_add_job_title(page_logged, job):
    """Crea varios Job Titles desde `data/job_titles.json`.
    """
    if job.get("valid") is False:
        pytest.xfail("Test data marcado como no válido; se espera fallo por nombre duplicado")
    page = page_logged.page

    home = HomePage(page)
    home.go_to_admin()
    home.open_job_dropdown()
    home.go_to_job_titles()

    jobs = JobTitlesPage(page)
    jobs.open_add_modal()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    titulo_unico = f"{job['title']} {timestamp}"
    jobs.fill_job_title(titulo_unico, job.get("description", ""), job.get("note", ""))
    # Si se quiere subir un archivo, descomentar y ajustar la ruta
    # jobs.upload_file("tests/resources/sample_file.txt")
    jobs.save_job_title()


