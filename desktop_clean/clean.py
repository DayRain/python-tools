import os
import datetime
import shutil


def get_config(file_name):
    """
    读取配置文件
    :param file_name: 文件名
    :return: 按行读取
    """
    f = open(file_name)
    lines = []
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)
    return lines


def get_desktop():
    """
    获取桌面路径
    :return: 桌面绝对路径
    """
    return os.path.join(os.path.expanduser("~"), 'Desktop')


def get_suffix(dir_path):
    """
    获取文件的后缀名
    :param dir_path: 文件名
    :return: 后缀名
    """
    return os.path.splitext(dir_path)[-1]


def get_exclude_suffix():
    """
    获取不参与整理的文件后缀名
    """
    dirs = {}
    lines = get_config('ignore.ini')
    for line in lines:
        dirs.setdefault(line, 0)
    return dirs


def get_target_path():
    """
    备份至指定文件夹
    :return: 目标位置的路径
    """
    return get_config('location.ini')[0]


def get_source_dirs():
    """
    获取需要转移的文件
    :return: 文件目录
    """
    dirs = os.listdir(get_desktop())
    suffixes = get_exclude_suffix()
    fit_dirs = []
    for dir in dirs:
        suffix = get_suffix(dir)
        if suffix not in suffixes and dir not in suffixes:
            fit_dirs.append(dir)
    return fit_dirs


def get_time():
    """
    获取当前年月日
    :return: 时间
    """
    return datetime.datetime.now().strftime('-%Y-%m-%d')


def get_rename(path):
    """
    文件重命名
    :param path: 路径
    :return: 命名后的路径
    """
    if os.path.isdir(path):
        return path + get_time()
    else:
        return os.path.splitext(path)[0] + get_time() + get_suffix(path)


def move():
    """
    移动文件
    """
    dirs = get_source_dirs()
    target_base_path = get_target_path()
    desk_url = get_desktop()
    if not os.path.exists(target_base_path):
        os.makedirs(target_base_path)

    for dir in dirs:
        path = os.path.join(desk_url, dir)
        target_path = os.path.join(target_base_path, dir)
        if os.path.exists(target_path):
            # 如果有同名文件，则加一个日期后缀
            target_path = get_rename(target_path)
        shutil.move(path, target_path)


if __name__ == '__main__':
    move()