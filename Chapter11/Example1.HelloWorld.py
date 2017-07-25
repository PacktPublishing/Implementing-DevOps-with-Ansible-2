#!/usr/bin/python
# The following Python code converts a simple "Hello Ansible" message into a json object 
# for use with an Ansible module call

import json

message = "Hello Ansible"
print(json.dumps({
  "Message" : message
}))