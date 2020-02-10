import pytest
import yaml
import os

with open("../data"+os.sep+"data.yaml", 'r',encoding='utf-8') as f:
    data1 = yaml.safe_load(f)
    print(data1)

