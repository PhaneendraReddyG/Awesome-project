def read_log(file_path):
    with open(file_path,"r") as file:
        return file.readlines()

def error_count(lines):
    return sum ( 1 for line in lines if "Error" in line)