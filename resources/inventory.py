#!/usr/bin/env python3

'''
Example custom dynamic inventory script for Ansible, in Python.
'''

import os
import sys
import argparse
import json

class ExampleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print(json.dumps(self.inventory));

    # Example inventory for testing.
    def example_inventory(self):
        return {
            'group': {
                'hosts': ['95.216.167.203', '142.132.183.83', '159.69.51.100', '116.202.9.249','167.235.196.204'],
                'vars': {
                    'ansible_user': 'root',
                    'ansible_ssh_private_key_file':
                        '~/.ssh/id_rsa',
                    'ansible_python_interpreter':
                        '/usr/bin/python3',
                    'example_variable': 'value'
                }
            },
            '_meta': {
                'hostvars': {
                    '142.132.183.83': {
                        'host_specific_var': 'testeumel'
                    },
                    '95.216.167.203': {
                        'host_specific_var': 'helsinki'
                    },
                    '116.202.9.249': {
                        'host_specific_var': 'foo'
                    },
                    '159.69.51.100': {
                        'host_specific_var': 'bar'
                    }
                }
            }
        }

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
ExampleInventory()
