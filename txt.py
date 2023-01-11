import os


def create_dir_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_files(root: str, dir: str, title: str, body: str, dir_1: str = "", dir_2: str = "", dir_3: str = "", dir_4: str = "", file_type: str = ".txt"):
    path = create_dir_if_not_exists(os.path.join(root, dir, dir_1, dir_2, dir_3, dir_4))
    file_path = os.path.join(path, title + file_type)
    with open(file_path, "w") as file:
        file.write(body)