

import logging, sys
from os import path, remove, walk

class ClassBrowser(object):
    def __init__(self):
        self.logname = path.basename(sys.argv[0][:-3]) + '.log'
        self.logger = None
        self.location = None
        self.folders = None
        self.target = None

    def get_dirs(self, location="S:\OBC"):
        self.location = path.normpath(location)
        if self.location[0] == "\\" and self.location [1] != "\\":
            self.location = "\\" + self.location

        #TODO: cannot read net work share folders
        self.logger.info('getting sub-dirs at {}'.format(self.location))
        self.folders = []
        for root, dirs, files in walk(self.location):
            for dir in dirs:
                self.folders.append(path.join(root, dir))
            print(self.folders)
            for file in files:
                self.folders.append(path.join(root, file))
                pass

        self.logger.info('found {} folders at {}'.format(len(self.folders), self.location))

    def show_dirs(self):
        self.logger.info('showing sub-dirs at {}'.format(self.location))
        for folder in self.folders:
            self.logger.debug(folder)

    def search(self, target):
        self.target = str(target).lower()
        for folder in self.folders:
            if self.target.lower() in str(folder).lower():
                print(folder)


    def configure_logger(self):
        # If applicable, delete the existing log file as it is overwritten each time
        if path.isfile(self.logname):
            remove(self.logname)

        # Create the Logger
        self.logger = logging.getLogger(self.logname[:-4])
        self.logger.setLevel(logging.DEBUG)

        # Create the Handler for logging data to a file
        logger_handler = logging.FileHandler(self.logname)
        logger_handler.setLevel(logging.DEBUG)

        # Create a Formatter for formatting the log messages
        logger_formatter = logging.Formatter('%(asctime)s %(name)s - %(levelname)s - %(message)s')

        # Add the Formatter to the Handler
        logger_handler.setFormatter(logger_formatter)

        # Add the Handler to the Logger
        self.logger.addHandler(logger_handler)
        self.logger.info('logger configuration_complete!')