# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging, os

PYFORMS_MODE                        = os.environ.get('PYFORMS_MODE', 'GUI')
PYFORMS_LOG_HANDLER_FILE_LEVEL      = logging.DEBUG
PYFORMS_LOG_HANDLER_CONSOLE_LEVEL   = logging.INFO
LOG_FILENAME                        = "pyforms.log"

CONTROL_CODE_EDITOR_DEFAULT_FONT_SIZE   = '12'
CONTROL_EVENTS_GRAPH_DEFAULT_SCALE      = 1


PYFORMS_QUALITY_TESTS_PATH = None

PYFORMS_STYLESHEET = None