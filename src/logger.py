import logging
import os
from datetime import datetime
log_file = f"{datetime.now().strftime('%d_%m_%Y_%H_%H_%m_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(logs_path,exist_ok=True)
log_file_path=os.path.join(logs_path,log_file)

logging.basicConfig(
    filename=log_file_path,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__=="__main__":
    logging.info("logging has started")
    