import os, logging, uuid
from Classes.ConfigurationData import ConfigurationData
from Classes.MainUser import MainUser
from Resources import *
from Utils.FileUtils import FileUtils
from Utils.StoredDataUtils import StoredDataUtils

from Mockups.Mockups import Mockups

class Environment():

    __mConfigurationData: ConfigurationData = None
    __mMainUser: MainUser = None
    __mLogger = None

    def __new__(cls):
        if not hasattr(cls, '_mInstance'):
            cls._mInstance = super(Environment, cls).__new__(cls)
        return cls._mInstance

#region - Getter Methods
    def get_configuration(self):
        return self.__mConfigurationData

    def get_main_user(self):
        return self.__mMainUser

    def get_logger(self):
        return self.__mLogger
#endregion

#region - Setter Methods
    def set_main_user(self, mainUser):
        self.__mMainUser = mainUser
#endregion

#region - Public Methods
    def set_main_user(self, id, name, surname, username):
        self.__mMainUser = MainUser()
        self.__mMainUser.setId(id)
        self.__mMainUser.setName(name)
        self.__mMainUser.setSurname(surname)
        self.__mMainUser.setUsername(username)

    def init(self):
        self.__init_directories()
        self.__init_configuration_data()
        self.__init_logger()
        self.__init_main_user()
#endregion

#region - Private Methods
    def __init_configuration_data(self):
        self.__mConfigurationData = ConfigurationData.get_stored_data()

    def __init_main_user(self):
        self.__mMainUser = MainUser.get_stored_data()
        if self.__mMainUser == None:
            self.__mMainUser = MainUser(uuid.uuid4())
            self.__mMainUser.set_tot_capital(Mockups.MOCKUP_USER_CAPITAL)
            self.__mMainUser.store_data()
        self.__mMainUser.set_from_stored_platform_data()
            
    def __init_logger(self):
        logging.basicConfig(level=logging.INFO)
        self.__mLogger = logging.getLogger()

    def __init_directories(self):
        StoredDataUtils.check_make_stored_data_dir_exists()
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {Environment.__name__}\n"\
                f"{super().__str__()}\n"\
                f"#- __mMainUser: {str(self.__mMainUser)}\n"\
                "####################"
