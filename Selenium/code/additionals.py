import json

def get_login_and_password_from_file(file_path):
    data_dict = {}

    with open(file_path, 'r') as file:
        data_dict = json.load(file)
    #     for line in file:
    #         key, value = line.strip().split(': ')
    #         data_dict[key] = value

    return data_dict