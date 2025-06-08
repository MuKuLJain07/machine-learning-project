# import logging 
# import os
# from datetime import datetime

# LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
# logs_path=os.path.join(os.getcwd(),"logs")
# os.makedirs(logs_path,exist_ok=True)

# LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO
# )


import logging
import os
from datetime import datetime

# Create a log file with only the date (not time) in the name
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d')}.log"  # Example: 2025_06_08.log

# Create logs directory if it doesn't exist
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full path to the daily log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging to append logs to the daily log file
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)