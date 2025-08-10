print("keys_change_check.py script text output")

import os

result_file = open(os.environ['GITHUB_OUTPUT'], 'a')

result_file.write("\n\nkeys_change_check.py result.md file output\n\n")

result_file.close()
