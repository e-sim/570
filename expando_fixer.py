import sys
import re

def give_output(matchobj):
    return (matchobj.group(1) + " " + matchobj.group(1) + ')')

FST_FILE = open(sys.argv[1], "r")

FST_EDGE_PATTERN = re.compile(r"(\w) \*e\*\)")

for line in FST_FILE:
    #edge_match = FST_EDGE_PATTERN.search(line)
   # if edge_match:
    print(FST_EDGE_PATTERN.sub(give_output, line)),
    #else:
     #   print(line)



FST_FILE.close()