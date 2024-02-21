import tkinter as tk
from tkinter import filedialog as fd
import os, zipfile

ERRMSG = 'Error!' # (for now)

def zip_dir(directory, config):
    print("Zip Dir")
    output = directory + '.zip'

    with zipfile.ZipFile(output, 'w', zipfile.ZIP_STORED) as archive: # TODO make unit test for this, including if files are "Stored" or compressed, if possible
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                archive.write(os.path.join(dirpath, filename), os.path.relpath(os.path.join(dirpath, filename), directory)) # TODO: make cbz support too?

    if config["delete"]:
        # delete files in directory
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                os.remove(os.path.join(dirpath, filename))

        # delete subdirectories
        for dirpath, dirnames, filenames in os.walk(directory):
            for dirname in dirnames:
                os.rmdir(os.path.join(dirpath, dirname))

        # delete directory
        os.rmdir(directory)

class NoZip:
    def __init__(self, config):
        # self.directory = directory
        self.config = config

    def zip(self):
        zip_dir(self.directory, self.config)

    def callback(self):
        name= fd.askdirectory()
        print(f'Directory: {name}')
        zip_dir(name, self.config)

def main():
    config = {
        "delete": True
    }
    nz = NoZip(config)
    tk.Button(text='Click to Open File', command=nz.callback).pack(fill=tk.X)
    tk.mainloop()

if __name__ == '__main__':
    main()