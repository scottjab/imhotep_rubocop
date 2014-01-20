from imhotep.tools import Tool
from collections import defaultdict
import json
import os


class RubyLintLinter(Tool):

    def invoke(self, dirname, filenames=set()):
        retval = defaultdict(lambda: defaultdict(list))

        cmd = "find %s -name '*.rb' | xargs rubocop -f j" % dirname
        try:
            output = json.loads(self.executor(cmd))
            for linted_file in output['files']:
                # The path should be relative to the repo,
                # without a leading slash
                # example db/file.rb
                file_name = os.path.abspath(linted_file['path'])
                file_name = file_name.replace(dirname, "")[1:]
                for offence in linted_file['offences']:
                    line_number = str(offence['location']['line'])
                    retval[str(file_name)][line_number].append(
                        str(offence['message']))
        except:
            pass
        return retval
