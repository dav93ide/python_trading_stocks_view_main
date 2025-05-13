import os, logging, uuid
from Resources import *
from Utils.FileUtils import FileUtils

class Environment():

    __mLogger = None

    def __new__(cls):
        if not hasattr(cls, '_mInstance'):
            cls._mInstance = super(Environment, cls).__new__(cls)
        return cls._mInstance

#region - Getter Methods
    def get_configuration(self):
        return self.__mConfigurationData

    def get_logger(self):
        return self.__mLogger
#endregion

#region - Public Methods
    def init(self):
        self.__init_logger()
#endregion

#region - Private Methods
    def __init_logger(self):
        logging.basicConfig(level=logging.INFO)
        self.__mLogger = logging.getLogger()
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {Environment.__name__}\n"\
                f"{super().__str__()}\n"\
                "####################"
