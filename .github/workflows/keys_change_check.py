import imp

print("keys_change_check.py script text output")

module_path = 'pr/.github/workflows/translation_check.py'

keys_pr_module = imp.load_source('keyspr', module_path)

print(keys_pr_module.KEYS_TO_IGNORE)

result = '#### Check results\n\n'

text_file = open("result.md", "w")
text_file.write(result)
text_file.close()
