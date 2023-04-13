#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyjson5
import pystache
import sys
import json

def parse(src, var_dic):
    data = pyjson5.decode(src)
    data_reps={}
    if "vars" in data:
        var_dic.update(data["vars"])
        reps = pystache.render(src, var_dic)
        data_reps = pyjson5.decode(reps)
        data_reps["vars"] = var_dic
        data = data_reps
    
    if "include" in data_reps:
        rep={}
        for fpath in data_reps["include"]:
            with open(fpath,"r") as f:
                rep.update(parse(f.read(), var_dic))
        del data_reps["include"]

        data_reps.update(rep)
        data=data_reps

    if "vars" in data:
        var_dic.update(data["vars"])
        reps = pystache.render(json.dumps(data), var_dic)
        data_reps = pyjson5.decode(reps)
        data_reps["vars"] = var_dic
        data = data_reps
    
    return data

if __name__ == "__main__": 
    if len(sys.argv) == 1:
        var_dic = {}
        dic=parse(sys.stdin.read(), var_dic)
        print(pyjson5.encode(dic))


    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            var_dic = {}
            dic=parse(f.read(), var_dic)
            print(pyjson5.encode(dic))


