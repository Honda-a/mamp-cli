"""
api wraper for mamp tools
"""
from mamp_cli.base import ApiBase
from configparser import ConfigParser


class ConfigApi(ApiBase):
    def __init__(self):
        self.conf_file = self.get_conf_file()
        self._conf = ConfigParser.read(self.conf_file)

    @property
    def conf(self):
        return self._conf

    @conf.getter
    def conf(self, section=''):
        if section and section in self._conf.sections():
            return self._conf['section']
        elif(section):
            return False
        else:
            return self._conf

    def change_config_path(self):
        pass

    def get_conf_file(self):
        pass
