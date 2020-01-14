#! /usr/bin/env python
# -*- coding' utf-8 -*-

import os
import commands #python3の場合はimport subprocess
import ambient

ambi = ambient.Ambient(ID, "write key")

temp = commands.getoutput("vcgencmd measure_temp").split('=')
temp2 = temp[1][:-2]

r = ambi.send({"d1": temp2})
