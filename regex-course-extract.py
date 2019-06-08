# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
from pprint import pprint

regex = r"([A-Z]{3})\s*([0-9]{3})\s*([a-zA-Z\s\W\(8]+)\s*([0-9]{1})"

test_str = ("RCS 100Introduction to Informatics2RCS 110Microcomputer Applications 2RCS 106 Calculus 3RCS 101 Computer Architecture 2RCS 104 Discrete Structures 3RMS 110 Introduction to Business and Management 2RPH 113Social Ethics I 2RSS 110Development Studies I 3RLG108Communication Skills I 3RCS 102 OO Programming I       3RCS 103 Algorithms & Data Structures   3RMS 222  Small Businesses & Entrepreneurship 2RCS 105Linear Algebra      3RPH 114Social Ethics II        2RSS 130 Development Studies II    3RLG 128Communication Skills II    3\n"
	"FIRST PRACTICAL TRAINING RPT 199 First Year Practical Training (8 weeks) 2Second Year (Semester Three)RCS 200 Network Design & Administration I  3RCS 203 Software Engineering     3RCS 207Structure of Programming Languages     2RCS 202 Operating Systems      3RCS 215Probability and Statistics      2Second Year (Semester Four)RCS 204 MIS         2RCS 201 Database Design         3RCS 208 Computer Graphics and Multimedia 2RCS 206 PC Diagnostics & Maintenance    2RCS 205 Linux System Administration  2SECOND PRACTICAL TRAINING RPT 299 Second Year Practical Training (8 weeks)2SECOND YEAR OPTIONAL COURSES RCS 209 Advanced Software Engineering  3RCS 210 Programming in C        3RCS 211 GIS              2RCS 213 Compilers            2RCS 214 Theory of Computation        2RCS 216Numerical Analysis      2Third Year (Semester Five)RCS 305 Computer System Security     2RCS 300 Systems Analysis and Design   3RCS 304 Professional Practices of Information Systems 2RCS 399 Final ICT Project     4Third Year (Semester Six)RCS 315Network Design & Administration II     2RCS 302Database Systems      3RCS 301 Internet Programming and E-Applications   2THIRD YEAR OPTIONAL COURSESRCS 303 Project Management      2RCS 310Computer Simulation and Modelling  2RCS 311 Introduction Artificial Intelligence     2RCS 307 Operations Research2RCS 313 Distributed Systems       2RCS 315Network Design & Administration II     2")

matches = re.finditer(regex, test_str, re.MULTILINE)
findallmatch = re.findall(regex, test_str, re.MULTILINE)
# pprint(findallmatch)
print("-"*68)
print("| {}   |{:>25}{:>25} {} |".format("CODE", "NAME", "|", "UNITS"))
print("-"*68)

for match in findallmatch:
    code, codeint, name, units = match
    pad = 48 - len(name)
    print("| {}{} | {} {:>{pad}} {} |".format(code, codeint, name, "|", units, pad=pad))
print("-"*68)
# for matchNum, match in enumerate(matches, start=1):
#     code, codeint, title, units = match.groups()
#     # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), 
#     # end = match.end(), match = match.group()))
#     # print ("{code} {codeint} {title} {units}".format(code = code.strip(), codeint = codeint.strip(), 
#     #     title = title.strip(), units=units.strip()))
#     # for groupNum in range(0, len(match.groups())):
#     #     groupNum = groupNum + 1
        
# for found in findallmatch:
#     print(found)        

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.


# Match all closing tags and comments(?:</\S+>)|(?:<!--.*-->)
