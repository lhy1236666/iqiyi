import os

def get_all_file_names(folder_path):
    file_names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_names.append(os.path.join(root, file))
        # for d in dirs:
        #     file_names.extend(get_all_file_names(os.path.join(root, d)))
    return file_names




def clear():
    # 指定文件夹路径
    starting_folder = './data'

    # 获取文件夹及其子文件夹下所有文件名
    all_files = get_all_file_names(starting_folder)

    # 打印所有文件名
    for file_name in all_files:
        # 以写入模式打开文件并清空内容
        with open(file_name, 'w') as file:
            file.write('')  # 写入空内容
