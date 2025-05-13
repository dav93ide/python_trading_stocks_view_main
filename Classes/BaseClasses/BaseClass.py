from typing import TypeVar, List
from multipledispatch import dispatch
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

    # To String
    def __str__(self):
        return  "####################\n"\
                f"# {BaseClass.__name__}\n"\
                f"#- __id: {self.__id}\n"\
                "####################"