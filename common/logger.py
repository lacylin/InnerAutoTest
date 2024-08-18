# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler

from common.settings import LOG_PATH

# 创建Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 终端Handler
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

# 文件Handler
fileHandler = RotatingFileHandler(LOG_PATH, maxBytes=1024 * 1024 * 10, backupCount=5)
fileHandler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# 添加到Logger中
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)
