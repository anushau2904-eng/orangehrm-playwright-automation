import logging
import os

class Logger:

    @staticmethod
    def get_logger():

        Log_dir = "logs"

        os.makedirs(Log_dir, exist_ok=True)
        log_file = os.path.join(Log_dir,"api_automation.log")

        logger = logging.getLogger("api_framework")

        if not logger.handlers:

            logger.setLevel(logging.INFO)

            file_handler = logging.FileHandler(log_file)
             
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger