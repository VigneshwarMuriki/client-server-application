import os
import time
from doctest import testmod


class TestServer:
    """
    >>> t = TestServer("Vignesh")
    >>> s = t.create_folder('Viggi')
    >>> s
    True
    >>> w = t.write_file("Viggi","Vigi",'Hi My name is Vignesh')
    >>> w
    True
    >>> r = t.read_file("viggi","Vigi")
    >>> r
    'Hi My name is Vignesh'
    >>> c = t.change_folder_path("Viggi")
    >>> c
    True
    """
    def __init__(self, user_id):
        """We create a user id for each person and save it
           into root file.

           input : user_id
           output : A file stored inside the root folder
        """
        self.user_id = user_id
        self.bool = 0
        self.file_name = 0
        self.filename = 0
        self.inp = 0
        self.size = 0
        self.curr = 0
        self.data_info = 0
        self.path_mod = 0
        self.path = 0
        self.is_write = 0
        self.file = 0
        self.modified = 0
        self.old_name = 0
        self.folder = 0
        self.root_path = f"C:\\Users\\ADMIN\\Downloads\\my assignment\\Assignment_3\\root\\{self.user_id}\\"
        try:
            os.makedirs(self.root_path)
        except Exception:
            pass

    def create_folder(self, name):
        """
        We create a folder where we store the files which are
        used to read and write using read_file and write_file
        functions.

        parameters:name
        Output: We create a folder name and the output will be
        printed if it satisfies the conditions.
        """
        self.file_name = name
        self.bool = False
        self.file = os.path.join(self.root_path, self.file_name)
        try:
            os.makedirs(self.file)
            self.bool = True
        except FileExistsError:
            print("File already exists")
        finally:
            return self.bool

    def write_file(self, file_name, new_name, input_id):
        """
        The write operation is performed by giving the foldername
        as input and file to be created and also the data
        to be written to the file.

        parameters: file_name, new_name, input_id

        Output: For given folder name, the file is written to the file
        created inside the folder and the output will be printed
        stating that the write_file is executed.
        """
        self.filename = new_name
        self.file_name = f"{file_name}\\"
        self.inp = input_id
        self.is_write = False
        try:
            self.path_mod = os.path.join(self.root_path, self.file_name)
            self.path = os.path.join(self.path_mod, self.filename)
            with open(self.path, 'w') as is_write:
                is_write.write(self.inp)
                self.is_write = True
        except Exception as exp:
            print(exp)
        finally:
            return self.is_write

    def read_file(self, file_name, new_name):
        """
        We perform read operation by specifying the folder name where
        we want to read the file.
        The read_file takes two arguments.
        parameters: file_name, new_name
        Returns: To read a file we need the folder name and also the
        file name created
        """
        self.filename = new_name
        self.file_name = f"{file_name}\\"
        self.data_info = ''
        try:
            self.path_mod = os.path.join(self.root_path, self.file_name)
            self.path = os.path.join(self.path_mod, self.filename)
            with open(self.path, 'r') as is_read:
                self.data_info = is_read.readlines()
        except Exception as exp:
            return print(exp)
        finally:
            return " ".join(self.data_info)

    def list_of_directories(self):
        """
        Here we print the existing list of directories present in the folder.
        The list of directories contain the name of file, creation, and also
        the size of file
        """
        self.file = os.listdir(self.root_path)
        self.size = []
        self.curr = []
        self.modified = []
        total_size = 0
        for file in self.file:
            self.folder = os.path.join(self.root_path, file)
            self.modified.append(time.ctime(os.path.getmtime(f"{self.folder}")))
            self.curr.append(time.ctime(os.path.getctime(f"{self.folder}")))
            for path, dirs, files in os.walk(self.folder):
                for file in files:
                    file_path = os.path.join(path, file)
                    total_size += os.path.getsize(file_path)
            self.size.append(total_size)
        return self.file, self.size, self.curr, self.modified

    def change_folder_path(self, old_name):
        """
        To change a folder path we specify which folder to be changed
        It takes one arguments i.e,; the folder name.
        """
        self.old_name = old_name
        self.curr = False
        os.chdir(self.root_path)
        try:
            os.chdir(old_name)
            self.curr = True
        except Exception:
            pass
        finally:
            return self.curr
if __name__ == "__main__":
    testmod(name='TestServer', verbose=True)
