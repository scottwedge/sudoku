#!/usr/bin/env python3


# Practice formatting to determine why get error message of
# "TypeError: unsupported format string passed to list.__format__

a = [[1], [2], [3]]
b = [[4],[5],[6],[7]]

print(a)

print("{}".format(a))


print("{:20}".format(str(b)))  # works if convert list to string before print

print("{:20}".format(b))
