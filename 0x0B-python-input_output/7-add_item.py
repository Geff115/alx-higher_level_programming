#!/usr/bin/python3
"""Importing sys module and other functions
to add arguments to a Python list.
"""


import sys
import os
import importlib

save_to_json_file = importlib.import_module('5-save_to_json_file').save_to_json_file
load_from_json_file = importlib.import_module('6-load_from_json_file').load_from_json_file


args_list = []
if os.path.exists('add_item.json'):
    data = load_from_json_file('add_item.json')
    for i in range(1, len(sys.argv)):
        data.append(sys.argv[i])
    save_to_json_file(data, 'add_item.json')
else:
    for i in range(1, len(sys.argv)):
        args_list.append(sys.argv[i])
    save_to_json_file(args_list, 'add_item.json')
