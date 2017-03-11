import os


class TmpFile:
    def __init__(self, folder):
        self.folder = folder

    @staticmethod
    def generate_name():
        return "tmpFile"

    def __enter__(self):
        name = self.generate_name()
        self.full_name = os.path.join(self.folder, name)

        with open(self.full_name, "w") as f:
            f.write("test str")
            pass

        return self.full_name

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.full_name)

with TmpFile("someDir/") as path:
    with open(path, "a") as f:
        f.write("123")

    with open(path, "r") as f:
        print(f.read())