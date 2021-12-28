class FileReader:
    def __init__(self, file_path):
        self.filePath = file_path
    
    def ReadFile(self):
        f = open(self.filePath, 'r', encoding ='utf-8')
        arr = f.read().split('\n')
        f.close()
        return arr