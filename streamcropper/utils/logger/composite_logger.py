class CompositeLogger():
    def __init__(self):
        self.loggers = []

    def add_logger(self, logger):
        self.loggers.append(logger)

    def info(self, message):
        for logger in self.loggers:
            logger.info(message)

    def error(self, message):
        for logger in self.loggers:
            logger.error(message)