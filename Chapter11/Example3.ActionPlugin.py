#!/usr/bin/python

# Import the Ansible Runner return data lib 
from ansible.runner.return_data import ReturnData

# Define our ActionModule class (MUST BE NAMED ActionModule)
class ActionModule(object):

    # Define our Calss constructor method (Must be present)
    def __init__(self, runner):
        self.runner = runner

    # Define our run method (must be present)
    def run(self, conn, tmp, module_name, module_args, inject, complex_args=None, **kwargs):
        return ReturnData(conn=conn, comm_ok=True, result=dict(failed=False, changed=False, msg="Hello Ansible"))