#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from hello import appl

httpd = make_server("", 12345, appl)

print "Server HTTP on port 12345..."

httpd.serve_forever()

