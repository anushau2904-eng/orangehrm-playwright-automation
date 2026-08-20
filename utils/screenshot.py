from pathlib import Path
from datetime import datetime
import allure


class ScreenshotUtil:


    PROJECT_ROOT = Path(__file__).resolve().parent.parent


    @classmethod
    def capture(cls, page, file_name):

        screenshot_dir = cls.PROJECT_ROOT / "screenshots"

        screenshot_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        screenshot_path = screenshot_dir / f"{file_name}_{timestamp}.png"


        page.screenshot(path=str(screenshot_path))

        allure.attach.file(
            str(screenshot_path),
            name=file_name,
            attachment_type=allure.attachment_type.PNG
        )