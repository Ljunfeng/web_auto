# ��Ŀ˵��

web�Զ�����Ŀ

��� pytest --html=report.html --self-contained-html

����Ŀ��Ŀ¼����
--html=report.html  ָ�����Ա���·��������
--self-contained-html  ��htmlҳ�汾�ؼ���css��ʽ

## pytest�汾����
    pytest==4.5.0
    allure-pytest==2.8.6
    PyYAML==5.3.1
    pytest_remotedata==0.3.2   #0.2.1���Ͱ汾�ᱨ��
    pytest-html==1.10.0
## ����requirements.txt�ļ�
    pip freeze > requirements.txt
    
    ��װ������
    pip install -r requirements.txt

## ��Ŀ�ṹ
- common ====>> ��װ��������
- case ====>> ��������
- pytest.ini ====> ����ִ����Щ�����������Լ����������
- config ���������ļ�����������������
### markers �����Ǹ�������ݼ�ע�ͣ�ȥ������
    ��������Ϊwebapi testcase
    @pytest.mark.webapi
    marks = 
        webapi: run web api testcase 
        ;�������д��Ϊ�����й����в������棬�ֺ�Ϊע�ͼ�


## pytest /allureһЩ������¼ 
## �ο� https://www.cnblogs.com/xiaogongjin/p/11705134.html
    1��@pytest.fixture(conftest.py��ĺ�����)   @pytest.usefixture(conftest.py��ĺ�����)
    ���һ������class����Ҫ�õ�fixture��ÿ��������ȥ���Σ���Ƚ��鷳�����ʱ�򣬿�����class�����usefixturesװ������������class������fixture
    ע�⣺��fixture��returnֵ��Ҫʹ��ʱ��ֻ�����������洫fixture�����ˡ���fixtureû��returnֵ��ʱ�����ַ���������
    
    2��@allure.feature(msg)
    �ӿ���������ģ�飬���磺��ȡ�û���Ϣ
    
    3��@allure.story(msg)
    �ӿڲ�����������
    
    4��@allure.description("������������ǲ�ʲô�ģ���һ�㲻д��@allure.story(msg)�㹻")
    ��������
    
    5��@allure.issue("https://www.xxx", name="�������ת����ӦBUG�����ӵ�ַ")
    �����ӿ�������Ӧ��bug����
    
    6��@allure.testcase("https://www.xxx", name="�������ת����Ӧ���������ӵ�ַ")
    ��������ϵͳ���Ӧ�������������ӡ�excel���������Ͳ���д��
    
    7�� @allure.severity(allure.severity_level.TRIVIAL)
    �������������ȼ�����һ��Ҳ��д
    
    8��@allure.epic("��Ե����ӿڵĲ���")
      ��������ĸ������ʷʫ��������feature