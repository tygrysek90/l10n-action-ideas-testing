import importlib.util

print("keys_change_check.py script text output")

module_path = 'pr/.github/workflows/translation_check.py'
module_name = 'keys_pr'  # You can choose any name for the module
module_spec = importlib.util.spec_from_file_location(module_name, module_path)
keys_pr_module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(keys_pr_module)

module_path = 'master/.github/workflows/translation_check.py'
module_name = 'keys_master'  # You can choose any name for the module
module_spec = importlib.util.spec_from_file_location(module_name, module_path)
keys_master_module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(keys_master_module)


# takes list of STR_nnnn in keys_list_old, compares to keys_list_new_unsorted
# takes data from en-GB.txt
# produces diff-style output
# produces new list ready to be inserted into code in translation_check.py

# by tygrysek90, enjoy :)

keys_list_old = keys_master_module.KEYS_TO_IGNORE
keys_list_new = keys_pr_module.KEYS_TO_IGNORE

keys = keys_list_new.copy()
# use github codeblock diff style
result_file = open("result.md", "w")

result = ("```diff")

OPENRCT2_EN_GB_FILE = "OpenRCT2/data/language/en-GB.txt"


for line in open(OPENRCT2_EN_GB_FILE ):
    if line[0:8] in keys_list_old and line[0:8] in keys_list_new:
        result += ("  "+line) # =
    if line[0:8] in keys_list_old and line[0:8] not in keys_list_new:
        result += ("- "+line)
    if line[0:8] not in keys_list_old and line[0:8] in keys_list_new:
        result += ("+ "+line)
    if line[0:8] in keys_list_new:
        keys_list_new.remove(line[0:8])

result += "\n"

result += (" "+20*"-")
result += "\n"
result += ("KEYS NOT FOUND IN en-GB.txt")
result += "\n"

for key in keys_list_new:
    result += ("! "+key)
    result += "\n"

result += ("\n "+20*"-")
result += ("```")
result += ("\n\n\n")

result_file.write(result)
result_file.close()
