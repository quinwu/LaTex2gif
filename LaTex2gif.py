import os
import time
import re

pwd = os.getcwd()

dir_string = pwd + '/' +os.popen('ls *.md').readlines()[0]

readFile = dir_string[:len(dir_string)-1]
writeFile = pwd + '/README.md'

r = open(readFile,"r")
w = open(writeFile,"w")

text = r.read()

regex = r"(\$\$*)([A-Za-z0-9\\_+\.\-*,;&\/=<>\^{}\(\)|\s]*)(\$\$*)"
split_regex = r"\$\$*"
str_regex = r"[A-Za-z0-9\\_+\.\-*\/=<>\^{}\(\)|\s]*"
pattern = re.compile(regex)

def replace(matchobj):
    rep = matchobj.group(0)
    rep = re.sub(r'\\',r'\\\\',rep)
    rep = re.sub(r'_',r'\\_',rep)
    return '![](http://latex.codecogs.com/gif.latex?' + re.split(split_regex,rep)[1]+ ')'

result = pattern.sub(replace,text)

w.write(result)

r.close()
w.close()
 