



LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "stdout": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "": {
            "handlers": ["stdout"],
            "level": "DEBUG",
            "propagate": True
        },
        "module1": {
            "handlers": ["stdout"],
            "level": "DEBUG",
            "propagate": False
        }
    },
}
