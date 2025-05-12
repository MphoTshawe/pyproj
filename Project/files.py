
import os
from importedfiles import ImportedFiles

class File:
    def __init__(self, filename, region):
        self.filename = filename
        self.region = region

    def get_region_code_from_filename(self):
        parts = self.filename.split('_')
        if len(parts) == 4 and parts[0] == 'sales' and parts[3].endswith('.csv'):
            region_code = parts[3][0]
            return region_code
        else:
            return None

    def is_valid_filename(self):
        
        parts = self.filename.split('_')
        
        if (
            len(parts) == 4 and             
            parts[0] == 'sales' and        
            parts[3].endswith('.csv')     
        ):
            region_code = parts[3][0]     
            if region_code in ['w', 'm', 'c', 'e']:
                return True
        return False
    
    def is_file_already_imported(self):
        
        importer = ImportedFiles()
        return importer.is_file_already_imported(self.filename)
    
     
    def is_file_found(self):
        return os.path.exists(self.filename)

class FileImportError(OSError):
    def __init__(self, message):
        super().__init__(message)
