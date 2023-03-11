import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize('env', yaml.safe_load(open('./env.yml')))
    def test_demo(self, env):
        if 'test' in env:
            print(f'这是测试环境，ip是{env}')
        elif 'dev' in env:
            print(f'这是开发环境，ip是{env}')

