#!/usr/bin/env python
# coding: utf-8

import pysnooper

@pysnooper.snoop()
def foo(bar, buz):
    if bar> buz:
        bar += buz
    else:
        buz *= bar
    return bar + buz

foo(3, 4)
foo(5, 4)