import re
import pprint

regex = r".*[a-z]+\s+([0-9]+)\s+[A-Z]{1}[a-z]{2}"

test_str = ("Directory of flash:/\n\n"
	"    5  -rwx        1048   Mar 1 1993 00:01:19 +00:00  multiple-fs\n"
	"    3  -rwx    14610929   Mar 1 1993 00:05:14 +00:00  c3750e-universalk9-mz.122-55.SE12.bin\n"
	"    4  drwx         512   Mar 7 1993 08:18:17 +00:00  c3750e-universalk9-mz.122-55.SE5\n\n"
	"57671680 bytes total (42938880 bytes free)")

matches = re.finditer(regex, test_str, re.MULTILINE)
match_all = re.findall(regex, test_str, re.MULTILINE)
pprint.pprint(match_all) # ['1048', '14610929', '512']
# print size of the directory
dir_size = 0
for size in match_all:
    dir_size += int(size)
print("File system is {} bytes".format(dir_size))
print("File system is {:.3f}KB".format(dir_size/1024))
# transformed = test_str
# for matchNum, match in enumerate(matches, start=1):
    
#     print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
#     for groupNum in range(0, len(match.groups())):
#         groupNum = groupNum + 1
#         grp = match.group(groupNum)
#         transformed = re.sub(grp, "{:.0f}KB".format(int(grp)/1024), transformed)
#         print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group=grp))

# print(transformed)
