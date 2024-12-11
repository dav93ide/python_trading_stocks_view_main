from Classes.BaseClasses.BaseClass import BaseClass
from Resources.Constants import DataFilenames

class ConfigurationData(BaseClass):

    __mIsInitialized = None


#region - Get Methods
    def get_is_initialized(self):
        return self.__mIsInitialized
#endregion

#region - Set Methods
    def set_is_initialized(self, initialized):
        self.__mIsInitialized = initialized
#endregion

#region - Public Methods
#region - Store Data Methods
    def store_data(self):
        BaseClass.store_data(self, DataFilenames.FILENAME_CONFIGURATION_DATA)

    @staticmethod
    def get_stored_data():
        return BaseClass.get_stored_data(DataFilenames.FILENAME_CONFIGURATION_DATA)
#endregion
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {Configuration.__name__}\n"\
                f"#- __mIsInitialized: {str(self.__mIsInitialized)}\n"\
                "####################"