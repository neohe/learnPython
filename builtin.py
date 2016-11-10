#!/usr/bin/env bash
# -*- coding: utf-8 -*-

import hashlib

md = hashlib.md5()
md.update("how to use md5 in python hashlib")

print md.hexdigest()

