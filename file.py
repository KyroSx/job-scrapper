class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_lines(self):
        with open(self.file_path, 'r') as file:
            lines = file.read().splitlines()
        return lines

    def write_lines(self, lines):
        with open(self.file_path, 'w') as file:
            file.write(lines)
