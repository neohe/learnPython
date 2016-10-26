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

