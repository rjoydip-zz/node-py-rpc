#!/usr/bin/env python

import sys

def execute(fn):
    def wrapper(*args, **kwargs):
        if len(sys.argv) > 1:
            method, params = sys.argv[1], sys.argv[2:]
            module_name = sys.modules[fn.__module__]
            methods = dir(module_name)
            if method in methods:
                nos_arg = getattr(module_name, methods[methods.index(method)]).__code__.co_argcount
                vars_name = getattr(module_name, methods[methods.index(method)]).__code__.co_varnames
                if nos_arg == 0 and method != 'main':
                    getattr(module_name, methods[methods.index(method)])()
                elif nos_arg == 1 and method != 'main':
                    getattr(module_name, methods[methods.index(method)])(params)
                elif nos_arg > 1 and method != 'main':
                    getattr(module_name, methods[methods.index(method)])(params, vars_name[1:])
                else:
                    print("Oops! can't access %s", method)
            else:
                print("Oops! {} method not exist in {} file.".format(method, module_name))
        else:
            return
        return fn()
    return wrapper