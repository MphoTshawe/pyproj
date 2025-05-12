
class ImportedFiles:
    def __init__(self):
        self.imported_files = []

    def is_file_already_imported(self, filename):
        if filename in self.imported_files:
            return True
        else:
            self.imported_files.append(filename)
            return False

