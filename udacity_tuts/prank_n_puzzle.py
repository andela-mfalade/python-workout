import os


# Modify this file path... Shouldn't be static
file_path = '/Users/Mayor/Desktop/codeVilla/python-workout/resources/prank/'


def get_files_in_directory():
    file_list = os.listdir(file_path)
    return file_list


def strip_num_from_file_name(file_name):
    num_str = '0123456789'
    return file_name.translate(None, num_str)


def rename_files():
    file_list = get_files_in_directory()
    for file_name in file_list:
        new_name = strip_num_from_file_name(file_name).replace(" ", "")
        old_file_path = file_path + file_name
        new_file_path = file_path + new_name
        os.rename(old_file_path, new_file_path)


def main():
    rename_files()


if __name__ == '__main__':
    main()
