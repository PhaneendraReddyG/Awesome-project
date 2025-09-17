def read_log(file_path):
    with open(file_path,"r") as file:
        return file.readlines()

def find_errors(lines):
    return [ line for line in lines if "Error" in line]