#!/usr/bin/python3
import dis
import marshal
import types
import sys
import os

if __name__ == "__main__":
    pyc_file = "/tmp/hidden_4.pyc"

    with open(pyc_file, "rb") as f:
        f.read(16)
        code = marshal.load(f)

    names = [name for name in code.co_names if not name.startswith("__")]
    for name in sorted(names):
        print(name)
