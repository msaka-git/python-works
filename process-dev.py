#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Find process and redirect pid number into a csv file.
'''

import os, signal, time, calendar, platform
from datetime import datetime

ts = calendar.timegm(time.localtime())
ts_local = datetime.utcfromtimestamp(ts).strftime('%Y%m%d%H%M%S')
ts_local2 = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')
host = platform.node()

def check_kill_process(pstring):
    for line in os.popen("ps ax | grep " + pstring + " | grep -v grep"):
        fields = line.split()
        global proc
        proc = fields[0]
        return proc
        # os.kill(int(proc), signal.SIGKILL)


def writing_logs():
    with open("/tmp/monitoring_logs." + ts_local, "a") as file:
        file.write("{};{};{} application;is running with;{}\n".format(ts_local2,host, i, proc))



def log_header():
    head=[""]
    with open("/tmp/monitoring_logs." + ts_local, "w") as file:
        file.write("Date;Hostname;Applications;Status;Commentaires\n")

log_header()
for i in ("firefox", "bash"):
    check_kill_process(i)
    writing_logs()
