#!/usr/bin/env python

import sys

def execute(fn):
    def wrapper(*args, **kwargs):
        module_name = sys.modules[fn.__module__]
        methods = dir(module_name)
        if len(sys.argv) > 1:
            method, params = sys.argv[1], sys.argv[2:]
            nos_arg = getattr(module_name, methods[methods.index(method)]).__code__.co_argcount
            vars_name = getattr(module_name, methods[methods.index(method)]).__code__.co_varnames
            if method in methods:
                if nos_arg == 0:
                    getattr(module_name, methods[methods.index(method)])()
                else:
                    if nos_arg == 1 and len(params):
                        getattr(module_name, methods[methods.index(method)])(params)
                    elif nos_arg > 1:
                        getattr(module_name, methods[methods.index(method)])(params, vars_name[1:])
                    else:
                        print("Please check you method properly.")
            else:
                print("Please check you method properly.")
        return fn()
    return wrapper