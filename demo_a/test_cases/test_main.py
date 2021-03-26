#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest

from demo_a.test_cases.test_base import TestBase
from demo_a.utils.get_data import get_yaml_data
from demo_a.utils.get_path import *

main_yaml_path = cases_dir + "/test_main.yaml"


class TestMain(TestBase):
    @pytest.mark.parametrize("value1, value2", get_yaml_data(main_yaml_path))
    def test_search(self, value1, value2):
        # app = App()
        # app.init().main().goto_search()
        print(value1)
        print(value2)

    def test_configuration(self):
        configuration = get_yaml_data(pages_dir + "/configuration.yaml")
        print(configuration)
