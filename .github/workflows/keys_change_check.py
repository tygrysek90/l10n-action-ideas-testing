import importlib.util

print("keys_change_check.py script text output")

module_path = 'pr/.github/workflows/translation_check.py'

module_name = 'keys_pr'  # You can choose any name for the module

# Create a spec for the module
module_spec = importlib.util.spec_from_file_location(module_name, module_path)

# Load the module from the spec
keys_pr_module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(keys_pr_module)

print(keys_pr_module.KEYS_TO_IGNORE)

result = '#### Check results\n\n'

text_file = open("result.md", "w")
text_file.write(result)
text_file.close()
