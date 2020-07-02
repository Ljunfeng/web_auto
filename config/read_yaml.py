import os
import yaml
import json
from configparser import ConfigParser
from common.logger import logger


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件内容自动转为小写的问题。来源百度
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class ReadFileData():

    def __init__(self, configfile):
        self.filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)),configfile)

    def load_yaml(self):
        logger.info(f"加载 {self.filepath} 文件......")
        with open(self.filepath, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logger.info(f"读到数据 ==>>  {data} ")
        return data

    def load_json(self):
        logger.info(f"加载 {self.filepath} 文件......")
        with open(self.filepath, encoding='utf-8') as f:
            data = json.load(f)
        logger.info(f"读到数据 ==>>  {data} ")
        return data

    def load_ini(self):
        logger.info(f"加载 {self.filepath} 文件......")
        config = MyConfigParser()
        config.read(self.filepath, encoding="UTF-8")
        data = dict(config._sections)
        return data

if __name__ == '__main__':
    data = ReadFileData('data_demo.yml')

