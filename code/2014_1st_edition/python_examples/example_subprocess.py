#!/usr/bin/env python
# Copyright (c) Marina von Steinkirch

__author__ = "bt3"

import subprocess,os

os.system('ls')
subprocess.call(['ls', '-1'], shell=True)
