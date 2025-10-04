from playwright.sync_api import Page

class JobTitlesPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_button = "button:has-text('Add')"
        self.job_title_input = "div[data-v-957b4417] input.oxd-input--active"
        self.job_description_input = "textarea[placeholder='Type description here']"
        self.job_note_input = "textarea[placeholder='Add note']"
        self.upload_button = "div.oxd-file-button"
        self.save_button = "button:has-text('Save')"


    def open_add_modal(self):
        """Abrir modal para añadir Job Title"""
        self.page.locator(self.add_button).click()
        self.page.locator(self.job_title_input).first.wait_for(state="visible", timeout=5000)

    def fill_job_title(self, title: str, description: str = "", note: str = ""):
        """Completar los campos del Job Title"""
        title_locator = self.page.locator(self.job_title_input).first
        title_locator.wait_for(state="visible", timeout=5000)
        title_locator.fill(title)
        if description:
            desc_locator = self.page.locator(self.job_description_input).first
            desc_locator.wait_for(state="visible", timeout=2000)
            desc_locator.fill(description)
        if note:
            note_locator = self.page.locator(self.job_note_input).first
            note_locator.wait_for(state="visible", timeout=2000)
            note_locator.fill(note)

    def upload_file(self, file_path: str):
        """Subir archivo en el modal"""
        file_input = self.page.locator(self.upload_button + " input[type='file']").first
        file_input.set_input_files(file_path)

    def save_job_title(self):
        """Guardar Job Title"""
        self.page.locator(self.save_button).click()
        try:
            self.page.locator(self.save_button).wait_for(state="detached", timeout=5000)
        except Exception:
            pass
