# 项目说明

web自动化项目

命令： pytest --html=report.html --self-contained-html

在项目根目录运行
--html=report.html  指定测试报告路径和名称
--self-contained-html  在html页面本地加载css样式

## pytest版本配置
    pytest==4.5.0
    allure-pytest==2.8.6
    PyYAML==5.3.1
    pytest_remotedata==0.3.2   #0.2.1过低版本会报错
    pytest-html==1.10.0
## 生成requirements.txt文件
    pip freeze > requirements.txt
    
    安装依赖包
    pip install -r requirements.txt

## 项目结构
- common ====>> 封装基础方法
- case ====>> 测试用例
- pytest.ini ====> 配置执行哪些测试用例，以及报告的命令
- config 所有配置文件都放在这里，方便管理。
### markers 作用是给标记内容加注释，去掉警告
    例如你标记为webapi testcase
    @pytest.mark.webapi
    marks = 
        webapi: run web api testcase 
        ;内容随便写，为了运行过程中不报警告，分号为注释键


## pytest /allure一些方法记录 
## 参考 https://www.cnblogs.com/xiaogongjin/p/11705134.html
    1、@pytest.fixture(conftest.py里的函数名)   @pytest.usefixture(conftest.py里的函数名)
    如果一个测试class都需要用到fixture，每个用例都去传参，会比较麻烦，这个时候，可以在class外面加usefixtures装饰器，让整个class都调用fixture
    注意：当fixture用return值需要使用时，只能在用例里面传fixture参数了。当fixture没有return值的时候，两种方法都可以
    
    2、@allure.feature(msg)
    接口用例所属模块，比如：获取用户信息
    
    3、@allure.story(msg)
    接口测试用例描述
    
    4、@allure.description("描述这个用例是测什么的，我一般不写，@allure.story(msg)足够")
    用例描述
    
    5、@allure.issue("https://www.xxx", name="点击，跳转到对应BUG的链接地址")
    该条接口用例对应的bug链接
    
    6、@allure.testcase("https://www.xxx", name="点击，跳转到对应用例的链接地址")
    用例管理系统里对应该条用例的链接。excel管理用例就不用写。
    
    7、 @allure.severity(allure.severity_level.TRIVIAL)
    测试用例的优先级，我一般也不写
    
    8、@allure.epic("针对单个接口的测试")
      敏捷里面的概念，定义史诗，往下是feature