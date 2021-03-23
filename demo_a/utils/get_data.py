#!/usr/bin/python
# -*- coding:utf-8 -*-
import yaml


def get_yaml_data(path):
    with open(path) as f:
        return yaml.safe_load(f)
