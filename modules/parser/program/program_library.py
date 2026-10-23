import os
from program import *

class ProgramLibrary:

    def __init__(self, program_folder:str):
        if not os.path.isdir(program_folder):
            return

        folder_entries = os.listdir(program_folder)
        program_folders = []

        for i in folder_entries:
            if os.path.isdir(i):
                program_folders.append(i)
        
        self.programs = []
        for i in program_folders:
            program = Program(i)
            if program:
                self.programs.append(Program(i))
        
