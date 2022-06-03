import os


class Views:
    clean_system_command = "cls" if os.name in ("nt", "dos") else "clear"

    def clear_console(self):
        os.system(self.clean_system_command)
        print("############ CHESS PROGRAM ############")
        print()
