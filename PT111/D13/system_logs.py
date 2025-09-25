import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s]\t%(levelname)s\t%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.info("Server started")
logging.warning("High memory usage")
logging.error("Connection lost")