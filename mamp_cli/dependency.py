"""

This module checks all dependencies

"""
from mamp_cli.api import OsApi


class Dependency:

    @staticmethod
    def check_wp_cli():
        if OsApi.command('wp --info'):
            return True
        else:
            return False


    @staticmethod
    def check_mamp():
        pass
