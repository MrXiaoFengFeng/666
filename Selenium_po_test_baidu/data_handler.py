import yaml

def get_data():
    with open('baidu_page.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        print(type(data))
        print(data['input'])
        print(data['input']['desc'])
        return data


get_data()


