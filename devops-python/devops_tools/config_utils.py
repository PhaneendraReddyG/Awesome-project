def validate_config(file_path):
    mandatory_keys = ['DB_HOST','DB_USER','DB_PASS']
    with open(file_path,'r') as file:
        lines = file.readlines()
    config_keys= [ line.split("=")[0].strip() for line in lines ]
    missing_keys =[ key for key in mandatory_keys if key not in config_keys]
    return f"The mentioned keys not found {missing_keys}"