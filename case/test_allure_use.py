import pytest
import allure

@pytest.fixture()
def login_fixture():
    print("先登录")

    yield
    print("用例测试完成之后数据清理")



def step_1():
    print("步骤1")


def step_2():
    print("步骤2")

def step_3():
    print("步骤3")


def step_4():
    print("步骤4")


@allure.feature("功能点：编辑文章分类页面")
class TestDemo():


    @allure.story("用例1：xxxxxxxxxxxxx")
    @allure.title("编辑文章分类，输入中文，编辑成功")
    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-6-2.html")
    def test_case1(self, login_fixture):
        '''用例描述：
        1	点文章分类导航标签 跳转编辑页面
        2	编辑页面输入，分类名称，如:文学，test, 123456 可以输入
        3	点保存按钮 保存成功，在列表页显示分类名称：文学
        '''
        with allure.step("步骤1：点点点"):
            step_1()
        with allure.step("步骤2：点点点"):
            step_2()
        with allure.step("步骤3：点点点"):
            step_3()

    @allure.story("用例1：xxxxxxxxxxxxx")
    @allure.title("编辑文章分类，输入英文，编辑成功")
    def test_case2(self):
        step_1()
        step_2()
        step_3()

    @allure.story("用例3：xxxxxxxxxxxxx")
    def test_case4(self):
        step_1()
        step_3()
        assert  1==2

