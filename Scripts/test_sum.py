import pytest,yaml
from Base.get_data import get_yaml

# def get_yaml():
#     lis = []
#     with open('./data/data.yaml', 'r', encoding='utf-8') as f:
#         data = yaml.safe_load(f)
#         for i in data.values():
#             lis.append(tuple(i.values()))
#     return lis

class TestSum():
    @pytest.mark.parametrize("a, b, c", get_yaml())
    def test_add(self, a, b, c):
        print("\n{}+{}={}".format(a, b, c))
        assert a + b == c
