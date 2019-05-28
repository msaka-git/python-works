#! /usr/bin/env python
#-*- coding: utf-8 -*-

import os, signal, time,calendar
from datetime import datetime

ts = calendar.timegm(time.localtime())
ts_local=datetime.utcfromtimestamp(ts).strftime('%Y%m%d%H%M%S')

def check_kill_process(pstring):
    for line in os.popen("ps ax | grep " + pstring + " | grep -v grep"):
        fields = line.split()
        global proc
        proc = fields[0]
        return proc
        #os.kill(int(proc), signal.SIGKILL)


def writing_logs():
    with open("/tmp/monitoring_logs." + ts_local,"a") as file:
        file.write("{} application is running with: {}\n".format(i,proc))

"""
def log_header():
    head=[""]
    with open("/tmp/monitoring_logs", "w") as file:
"""


for i in ("firefox", "bash"):
    check_kill_process(i)
    writing_logs()