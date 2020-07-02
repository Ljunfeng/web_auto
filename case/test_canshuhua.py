import pytest


@pytest.fixture(scope="session")
def login_first():
    '''前置操作'''
    print("\n前置操作：先登录")
    yield
    print("数据清理，执行你的数据库清理")


@pytest.fixture(scope="session")
def fuction_2():
    '''前置2'''
    print("前置操作2")


@pytest.fixture(scope="session")
def fuction_3(login_first, fuction_2):
    '''前置：调用上面2个前置'''
    print("前置：调用上面2个前置")



def add(a,b):
    '''定义函数，实现某个功能
    功能：相加'''
    return a+b



# 官方案例，标准格式
@pytest.mark.parametrize("test_input, expected",
                         [[{"a": 1, "b": 2}, 3],
                          [{"a": "1", "b": "2"}, "12"]
                          ],
                         ids = [
                             "用例1： 输入a=1, b=2,expected3",
                             "用例2： 输入a=\"1\", b=\"2\",expected12",
                         ]

)
def test_add(test_input, expected):
    result = add(test_input["a"], test_input["b"])  # 实际结果
    expect = expected                              # 期望结果
    assert result == expect


@pytest.mark.parametrize("a,b,expected",
                         [
                             [1, 2, 3],
                             ["1", "2", "12"],
                         ])
def test_x(fuction_3, a, b, expected):
    result = add(a, b)  # 实际结果
    expect = expected                              # 期望结果
    assert result == expect
