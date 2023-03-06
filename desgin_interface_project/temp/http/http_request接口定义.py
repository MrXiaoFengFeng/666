request_data = {
    'http_version': '2.0',
    'method': 'POST',
    'params': {
        'key1': 'v1',
        'key2': 'v2',
    },
    'data': {
        'key1': 'v1',
        'key2': 'v2',
    },
    'json': {
        'key1': 'v1',
        'key2': 'v2',
    },
    'headers': {
        'key1': 'v1',
        'key2': 'v2',
    },
    'cookies': {
        'key1': 'v1',
        'key2': 'v2',
    },
    'url': 'url'
}

import json

with open('数据驱动接口定义.json', 'w', encoding='utf-8') as f:
    json.dump(request_data, f)
    '''
    data = json.dumps(request_data)
    f = open('数据驱动接口定义.json','w',encoding='utf-8')
    f.write(data)
    '''
