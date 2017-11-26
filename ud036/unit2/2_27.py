import os
from string import digits

def rename_files_in_dir():
    files_list = os.listdir(r'/Users/thinkreed/Downloads/prank')
    print(files_list)
    current_path = os.getcwd()
    os.chdir(r'/Users/thinkreed/Downloads/prank')
    remove_digits = str.maketrans('', '', digits)
    for file_name in files_list:
        os.rename(file_name, file_name.translate(remove_digits))
    os.chdir(current_path)


def test():
    rename_files_in_dir()
    test_str = '2353587jjjjh4455'
    remove_digits = str.maketrans('', '', digits)
    print(test_str.translate(remove_digits))


test()
