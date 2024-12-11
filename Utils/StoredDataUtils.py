import pickle, os
from Utils.FileUtils import FileUtils
from Resources.Constants import Directories
from Resources.Constants import DataFilenames

class StoredDataUtils(object):

#region - Store Data Methods
    def check_stored_data_dir_exists():
        return FileUtils.check_file_exists(Directories.DIR_STORED_DATA)

    def check_stored_data_file_exists(path):
        return FileUtils.check_file_exists(FileUtils.join_filepath(Directories.DIR_STORED_DATA, path))

    def check_make_stored_data_dir_exists():
        if not StoredDataUtils.check_stored_data_dir_exists():
            os.mkdir(Directories.DIR_STORED_DATA)

    def store_data(data, path):
        with open(FileUtils.join_filepath(Directories.DIR_STORED_DATA, path), 'wb') as f:
            pickle.dump(data, f)

    def get_stored_data(path):
        ret = None
        p = FileUtils.join_filepath(Directories.DIR_STORED_DATA, path)
        if(FileUtils.check_file_exists(p)):
            with open(p, 'rb') as f:
                ret = pickle.load(f)
        return ret

    def remove_stored_data(path):
        ret = None
        p = FileUtils.join_filepath(Directories.DIR_STORED_DATA, path)
        os.remove(p)

    def add_to_stored_data_list(obj, path):
        if StoredDataUtils.check_stored_data_file_exists(path):
            data = None
            with open(FileUtils.join_filepath(Directories.DIR_STORED_DATA, path), 'rb') as f:
                data = pickle.load(f)
            if hasattr(data, "__len__"):
                data.append(obj)
                StoredDataUtils.store_data(data, path)
        else:
            StoredDataUtils.store_data([obj], path)

    def get_obj_from_id(id, cls, path):
        objs: [cls] = StoredDataUtils.get_stored_data(path)
        for obj in objs:
            if obj.get_id() == id:
                return obj

    def override_obj_from_id(id, obj, path):
        objs: [type(obj)] = StoredDataUtils.get_stored_data(path)
        pos = -0x1
        for i in range(0, len(objs)):
            if objs[i].get_id() == obj.get_id():
                pos = i
                break
        if pos != -0x1:
            objs[pos] = obj
        StoredDataUtils.store_data(objs, path)
                
#endregion