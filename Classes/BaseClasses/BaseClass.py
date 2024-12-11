from typing import TypeVar, List
from multipledispatch import dispatch
from Utils.StoredDataUtils import StoredDataUtils
from Resources.Constants import Directories, DataFilenames
from Utils.FileUtils import FileUtils

T = TypeVar('T')
class BaseClass():

    __id = None

    def __init__(self, id):
        self.__id = id

#region - Getter Methods
    def get_id(self):
	    return self.__id
#endregion
    
#region - Setter Methods
    def set_id(self, id):
        self.__id = id
#endregion

#region - Public Methods
#region - Store Data Methods
    @staticmethod
    def store_data(obj: T, path):
        StoredDataUtils.store_data(obj, path)

    @staticmethod
    def store_data_list(items: List[T], path):
        StoredDataUtils.store_data(items, path)

    @staticmethod
    def get_stored_data(path):
        return StoredDataUtils.get_stored_data(path)

    @staticmethod
    def add_to_stored_data_list(obj: T, path):
        StoredDataUtils.add_to_stored_data_list(obj, path)
#endregion
#endregion

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {BaseClass.__name__}\n"\
                f"#- __id: {self.__id}\n"\
                "####################"