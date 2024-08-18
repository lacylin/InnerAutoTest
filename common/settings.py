# -*- coding: utf-8 -*-

import os
import pathlib

BASE_DIR = pathlib.Path(__name__).parent

# 日志目录 =====================================
LOG_DIR = os.path.join(
    BASE_DIR,
    "log",
)
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

LOG_PATH = os.path.join(LOG_DIR, "runtime.log")
# ==============================================


# 报告目录 ============================================
REPORT_DIR = os.path.join(BASE_DIR, "report")
if not os.path.exists(REPORT_DIR):
    os.mkdir(REPORT_DIR)
ENVIRONMENT_PROPERTIES_PATH = os.path.join(REPORT_DIR, "environment.properties")
# =================================================
