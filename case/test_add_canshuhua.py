import pytest
from pages.articleclassify_page import ArticleClassifyPage
import allure
import os
from config.read_yaml import ReadFileData

readyml = ReadFileData('data_demo.yml')

a = readyml.load_yaml()
print(a['test_add_canshuhua'])


test_datas = a['test_add_canshuhua']
# 测试数据，单独拿出来
# test_datas = [
#     ["中文", True],
#     ["yingwen", True],
#     ["1234", True]
# ]


@pytest.fixture(scope="function")
def delete_some_data():
    print("连接你的数据库，清理数据")



@allure.story("用例：编辑文章分类-成功")
@allure.title("{title}")
@allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-6-2.html")
@pytest.mark.parametrize("input_text, expected, title",
                         test_datas,

                         )
def test_add_article_1(login_fixture, delete_some_data, input_text, expected, title):
    '''用例描述：
        1	点文章分类导航标签 跳转列表页面
        2   点编辑 文章分类按钮，跳转到编辑页面
        3	编辑页面输入，分类名称，如:文学，test, 123456 可以输入
        4	点保存按钮 保存成功，在列表页显示分类名称：文学
    '''
    driver = login_fixture
    # input_text = "中文"
    article = ArticleClassifyPage(driver)
    with allure.step("步骤1：点文章分类导航标签 跳转编辑页面"):
        article.click_articleclassify()
    with allure.step("步骤2: 点添加 文章分类按钮"):
        article.click_add_articleclassify()
    with allure.step("步骤3：编辑页面输入，分类名称，如:文学，test, 123456 可以输入"):
        article.input_article(input_text)
    with allure.step("步骤4: 点保存按钮 保存成功，在列表页显示分类名称：文学"):
        article.click_save_button()
    # 获取结果
    with allure.step("获取结果: 获取页面实际结果，判断是否添加成功"):
        result = article.is_add_success()
        print(result)
    with allure.step("断言：判断是否添加成功"):
        assert result == expected