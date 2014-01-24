from imhotep.tools import Tool
from collections import defaultdict
import json
import os


class RubyLintLinter(Tool):

    def invoke(self, dirname, filenames=set()):
        retval = defaultdict(lambda: defaultdict(list))

        if len(filenames) == 0:
            cmd = "find %s -name '*.rb' | xargs rubocop -f j" % dirname
        else:
            ruby_files = []
            for filename in filenames:
                if '.rb' in filename:
                    ruby_files.append("%s/%s" % (dirname, filename))

            cmd = "rubocop -f j %s" % (" ".join(ruby_files))
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
                    retval[str(file_name)][line_number] = list(set(retval[str(file_name)][line_number]))
        except:
            pass
        return retval
