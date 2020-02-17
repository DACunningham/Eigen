class FileIO(object):
    """Exposes methods to load single or multiple text files into memory"""

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)


    def load_text_file(self, file_location):
        """Loads text file and returns string contents to caller. 'file_location' is file location and file name to be loaded """
        file = open(file_location, 'rt', encoding = "utf8")
        file_text = file.read()
        file.close()
        return file_text

    def load_many_text_files(self, new_file_paths):
        """Load many text files as string into an array.  new_file_paths is an array of file locations and file names"""
        document_library = []
        for file_path in new_file_paths:
            document_library.append(self.load_text_file(file_path))
        return document_library
