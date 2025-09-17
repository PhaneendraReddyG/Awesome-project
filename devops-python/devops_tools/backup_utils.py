import os 

def backup_file(source_file):
    backup_file = source_file + ".backup"
    if os.path.exists(source_file):
        with open(source_file, 'r') as src, open(backup_file, 'w') as dst:
            dst.write(src.read())
        return f"Backup created at {backup_file}"
    return "Source file does not exist."