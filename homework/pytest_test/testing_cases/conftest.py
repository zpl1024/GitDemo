#支持ids显示为中文 开始
from typing import List

import pytest

from homework.pytest_test.python_code.calc_code import calculator


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
#支持ids显示为中文 结束

@pytest.fixture(scope='module')
def get_calc():
    calcu = calculator()
    return calcu