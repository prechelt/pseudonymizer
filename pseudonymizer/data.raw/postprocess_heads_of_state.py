import re
import sys

# call as: postprocess_heads_of_state wikidata-heads-of-state.txt ../data/personnames.txt
inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

#----- read raw query result data:
with open(inputfilename, encoding="utf8") as file:
    lines = file.readlines()

#----- extract names:
result = []
for line in lines:
    if line.startswith("#"):
        continue   # skip comments
    # line format: number TAB TAB name BLANK TAB description
    # description can be empty (but BLANK TAB will still be there)
    # name is one or more words or: actual name COMMA BLANK title
    mm = re.match("^(\d+)\t\t([^\t]+) \t(.*)\n?$", line)
    #mm = re.search("\t\t([\t]+)", line)
    assert mm, line  # other line formats should not exist
    name = mm.group(2)
    comma_position = name.find(",")
    if comma_position >= 1:
        name = name[:comma_position-1]  # cut off title part, if any
    result.append(name+'\n')

#----- write output file:
with open(outputfilename, "w", encoding="utf8") as file:
    file.writelines(sorted(result))