#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s','--scope',
    nargs='*',
    help='local or global',
    default=[]
)
args,remain = parser.parse_known_args()

print("declare -A optsdic=()\n")
if args.scope:
    if args.scope[0] == "local":
        print("local opts=$(getopt --longoptions \""+" ".join(remain)+"\" --options \"\" -- \"$@\" )")
    else:
        print("opts=$(getopt --longoptions \""+" ".join(remain)+"\" --options \"\" -- \"$@\" )")
else:
    print("opts=$(getopt --longoptions \""+" ".join(remain)+"\" --options \"\" -- \"$@\" )")

print("eval set --$opts\n")
print("while [[ $# -gt 0 ]]; do")
print("case \"$1\" in")
for a in remain:
    if a[-1] == ":":
        print("--"+a[:-1]+") optsdic[\""+a[:-1]+"\"]=$2 ; shift 2;;")
    else:
        print("--"+a+") optsdic[\""+a+"\"]=\"\" ; shift 1;;")
print("*)")
print("break ;;")
print("esac")
print("done")
