
print("explain.py - script output beings here:")

OPENRCT2_EN_GB_FILE = "OpenRCT2/data/language/en-GB.txt"

from translation_check import KEYS_TO_IGNORE as keys_to_explain

keys_explained = keys_to_explain.copy()

print(" "+20*"-")
print("Expanding items in KEYS_TO_IGNORE in translation_check.py using en-GB.txt")

for line in open(OPENRCT2_EN_GB_FILE):
    str_nnnn = line[0:8]
    if str_nnnn in keys_to_explain:
        print(line[:-1])
        keys_explained.remove(line[0:8])
        

print(" "+20*"-")
if len(keys_explained) > 0:
    print("Keys not found en-GB.txt, please consider purging:")
    for key in keys_explained:
        print(key)
    print("\n "+20*"-")
else:
    print("All keys sucessfully explained.")
