#!/usr/bin/python#!/usr/bin/python
import json
def main(): 

    module = AnsibleModule(argument_spec=dict( param1 = dict(required=True, type='str') ) )
    message = module.params['param1']

    print(json.dumps({
        "Message" : message
    }))

    module.exit_json(changed=True, keyword=value)
    module.exit_json(changed=False, msg='error message ', keyword=value)

from ansible.module_utils.basic import *
if __name__ = '__main__': 
    main() 