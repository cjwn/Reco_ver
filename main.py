import os


from pathlib import Path
import ctypes.wintypes

from SQLmanager import SqlWorker
from specs import KNOWNFOLDERID_LIST
from tools import Folders, Scan, time_it, str_of_size, scan_files, make_json, make_csv_by_batch


# def SHGetKnownFolderPath(fid):
#     buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
#     ctypes.windll.shell32.SHGetKnownFolderPath(fid, 0, None, buf)
#     return buf.value


def test():
    cwd = os.getcwd()
    for i in os.scandir(cwd):
        print(i.path, i.stat().st_size / 1024 / 1024)
        break


if __name__ == "__main__":
    cnn = SqlWorker('test4.db')
    cnn.init_files_db()
    info, total_info, total_file = scan_files(cnn)
    cnn.commit()
    make_csv_by_batch(total_file)
    make_json(total_info)
    print(info)


