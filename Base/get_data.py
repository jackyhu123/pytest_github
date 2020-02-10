import yaml


def get_yaml():
    lis = []
    with open('./data/data.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        for i in data.values():
            lis.append(tuple(i.values()))
    return lis

