from os import path

import pytest
from errbot.backends.test import testbot

extra_plugin_dir = path.join(path.dirname(path.realpath(__file__)), 'config_plugin')


def test_failed_config(testbot):
    assert 'Plugin configuration done.' in testbot.exec_command('!plugin config Config {"One": "two"}')
