#!/usr/bin/env python3
"""
tools.py - Phenny Tools
Copyright 2008, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""


def decorate(obj, delegate):
    class Decorator(object):
        def __getattr__(self, attr):
            if attr in delegate:
                return delegate[attr]

            return getattr(obj, attr)

        def __setattr__(self, attr, value):
            return setattr(obj, attr, value)

    return Decorator()

class GrumbleError(Exception):
    pass


def deprecated(old): 
    def new(phenny, input, old=old): 
        self = phenny
        origin = type('Origin', (object,), {
            'sender': input.sender, 
            'nick': input.nick
        })()
        match = input.match
        args = [input.bytes, input.sender, '@@']

        old(self, origin, match, args)
    new.__module__ = old.__module__
    new.__name__ = old.__name__
    return new

if __name__ == '__main__': 
    print(__doc__.strip())
