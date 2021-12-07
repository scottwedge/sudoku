#!/usr/bin/env python3

# Adjust column width in print statement

a = 1
b = 2
c = 3

print("{a:{b}{c}}".format(a=123, b=0, c=6))

print("{num:{width}}".format(num=123,  width=8))

print("{string1:{width}}".format(string1="[[123]]",  width=12))

print("{string1:>{width}}".format(string1="[[123]]",  width=22))
