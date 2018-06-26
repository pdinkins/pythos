'''
Writer module:
This module interacts with files and contians the classes
neccesasry for that intrction
'''

class FileObject:
    '''
    This class only creates a file object for refrencingby other 
    classes and functions. Do not use this function for anythong else
    '''
    def __init__(self, filename, filetype):
        self.filename = filename
        self.filetype = filetype
        self.file = self.fileconstructor()
        self.filecreator()

    def fileconstructor(self):
        return self.filename + '.' + self.filetype

    def filecreator(self):
        open(self.file, mode='w')

class Write2file:
    def __init__(self, filenameobject, data2write):
        with open(filenameobject, 'w') as fille:
            fille.write(data2write)

