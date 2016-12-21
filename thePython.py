#!/usr/bin/env python
# -*- coding: utf-8 -*-

def lazy_sum(*args):
	def sum():
		s = 0
		for n in args:
			s = s + n
		return s
	return sum

f = lazy_sum(1, 4, 7)
f1 = lazy_sum(1, 4, 7)
print f
print f1
print f()

print map(lambda x: x * x, [2, 4, 6])

print reduce(lambda x, y: x * 10 + y, [3, 2, 1])

def fn(x, y):
	return x * 10 + y

def char2num(s):
	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

print reduce(fn, map(char2num, '13468'))

print "Happy Birthday!"
print "cookie & session"
# openpilot

