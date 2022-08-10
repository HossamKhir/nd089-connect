#! /usr/bin/env python3
"""script to demonstrate variable scopes

https://www.toppr.com/guides/python-guide/references/methods-and-functions/global-local-nonlocal-variables/python-global-local-and-nonlocal-variables-with-examples/
"""

glob = "I am global"


def show_global():
    """ """
    print(glob)


def overwrite_global():
    """ """
    glob = "I am no longer global"


def edit_global():
    """ """
    glob += ", and I am proud"


if __name__ == "__main__":
    show_global()
    overwrite_global()
    show_global()
    edit_global()
    show_global()
