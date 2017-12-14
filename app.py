import taint
import inspect
import os
import sys

for m in [os, sys]: taint.mark_sinks(m)

#@taint.source
def user_input():
    return "ls -alt"

print("Untainted:")
os.system(user_input())

user_input = taint.source(user_input)

print("Tainted:")
x = user_input()
y = x + ""
z = y[0:2]
os.system(y)
