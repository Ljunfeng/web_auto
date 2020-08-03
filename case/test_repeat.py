import pytest
import time


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
    time.sleep(1)


def test_1(login_first):
    print("用例111111111")
    time.sleep(1)



def test_2(login_first):
    print("用例3333333333")
    time.sleep(1)
