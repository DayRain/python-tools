def load(file_name):
    dic = {}
    with open(file_name, 'r', encoding='utf-8') as fp:
        lines = fp.read().splitlines()
        for line in lines:
            if line.startswith('#') or line.strip() == '':
                continue
            line_list = line.split('=', maxsplit=1)
            dic.setdefault(line_list[0], line_list[1])
    return dic
