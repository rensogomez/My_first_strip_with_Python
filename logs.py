import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename=r'C:\Users\Renso\Programs\pc_performance\Logs\pc_performance.logs',
    filemode='w'
)

def log_debug(message):
    logging.debug(message)

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)

def log_critical(message):
    logging.critical(message)

if __name__== "__main__":
    logging
    