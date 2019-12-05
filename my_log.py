#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@Time  : 17/1/2 下午3:15
#@Author: wuchenglong

####################
# log config
####################

# Format	Description
# %(name)s	Name of the logger (logging channel).
# %(levelno)s	Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
# %(levelname)s	Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
# %(pathname)s	Full pathname of the source file where the logging call was issued (if available).
# %(filename)s	Filename portion of pathname.
# %(module)s	Module (name portion of filename).
# %(funcName)s	Name of function containing the logging call.
# %(lineno)d	Source line number where the logging call was issued (if available).
# %(created)f	Time when the LogRecord was created (as returned by time.time()).
# %(relativeCreated)d	Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.
# %(asctime)s	Human-readable time when the LogRecord was created. By default this is of the form “2003-07-08 16:49:45,896” (the numbers after the comma are millisecond portion of the time).
# %(msecs)d	Millisecond portion of the time when the LogRecord was created.
# %(thread)d	Thread ID (if available).
# %(threadName)s	Thread name (if available).
# %(process)d	Process ID (if available).
# %(message)s	The logged message, computed as msg % args.
import os
from io import StringIO as StringBuffer
log_capture_string = StringBuffer()


proj_dir = os.path.dirname(__file__)
_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[-%(levelname)s-] %(asctime)s %(process)d %(message)s'
        },
        'detail': {
            'format': '[-%(levelname)s-] %(asctime)s %(process)d ' + ' %(module)s.%(funcName)s line:%(lineno)d  %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            # 'formatter': 'simple'
            'formatter': 'detail',
            'stream': log_capture_string,
        },
        'console1': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                # 'formatter': 'simple'
                'formatter': 'detail',
                # 'stream': log_capture_string,
            },
        'file': {
            'level': 'DEBUG',
            'formatter': 'detail',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            # 'maxBytes': 1024,
            # 'backupCount': 3,
            'when': 'midnight',
            'interval': 1,
            'filename': os.path.join(proj_dir, 'log/debug.log')
        },
        'err_file': {
            'level': 'ERROR',
            'formatter': 'detail',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'filename': os.path.join(proj_dir, 'log/error.log')
        },
        'perf': {
            'level': 'INFO',
            'formatter': 'simple',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'filename': os.path.join(proj_dir, 'log/info.log')
        },
        'track': {
            'level': 'WARN',
            'formatter': 'simple',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'filename': os.path.join(proj_dir, 'log/warn.log')
        },

    },
    'loggers': {
        'default': {
            'level': 'DEBUG',
            'handlers': ['console1', 'file', 'err_file', 'perf', 'track']
        },
        'console': {
            'handlers': ['file', 'err_file'],
            'level': 'DEBUG'
        },
        'perf': {
            'handlers': ['perf'],
            'level': 'DEBUG',
            'propagate': False
        },
        'track': {
            'handlers': ['track'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}


import logging.config
logging.config.dictConfig(_LOGGING)
logger = logging.getLogger('default')

if __name__ == "__main__":
    logger.debug("======= test =========")
    logger.info("======= test =========")
    logger.error("======= test =========")

    log_contents = log_capture_string.getvalue()
    log_capture_string.close()
    # print(log_contents.lower())
