# This Code Example Comes from the Official Ansible Documentation Set (http://www.ansible.com/)

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()

# This is the standard class for the LookupModule implementation it is required to be this name 
class LookupModule(LookupBase):

    # As with all our other plugins, the run method MUST be there 
    def run(self, terms, variables=None, **kwargs):

        ret = []
        # Perform iteration
        for term in terms:

            display.debug("File lookup term: %s" % term)

            # Find the file in the expected search path
            lookupfile = self.find_file_in_search_path(variables, 'files', term)
            display.vvvv(u"File lookup using %s as file" % lookupfile)
            try:
                if lookupfile:
                    contents, show_data = self._loader._get_file_contents(lookupfile)
                    ret.append(contents.rstrip())
                else:
                    raise AnsibleParserError()

            except AnsibleParserError:
                raise AnsibleError("could not locate file in lookup: %s" % term)
return ret