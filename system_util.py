import os

class SystemUtil:
    @staticmethod
    def clear_terminal():
        os.system("cls" if os.name == "nt" else "clear")

