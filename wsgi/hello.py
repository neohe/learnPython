#!/usr/bin/env python
# -*- coding: utf-8 -*-

def appl(environ, start_response):
	start_response("200 OK", [("Content-Type", "text/html")])
	return "<h1>Hello, web!</h1>"

