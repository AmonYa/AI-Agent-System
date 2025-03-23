from loguru import logger

# Настраиваем логирование в файл logs/system.log
logger.add("logs/system.log", format="{time} {level} {message}", level="INFO", rotation="10 MB")
