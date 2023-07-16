import logging, os
from datetime import datetime
now = datetime.now()
log_file_name = f"{now.strftime('%a %d-%b-%Y %H-%M-%S')}"
log_path = os.path.join(os.getcwd(), 'logs', log_file_name)
os.makedirs(log_path, exist_ok=True)
log_file_path = os.path.join(log_path, log_file_name+'.log')

logging.basicConfig(
    filename=log_file_path,
    format='[%(asctime)s] [%(lineno)d %(name)s %(levelname)s] %(message)s',
    level=logging.INFO
)