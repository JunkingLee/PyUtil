import redis
import json
import datetime
import sys
import time
import subprocess
import shlex
import pdb

pool = redis.ConnectionPool(host='127.0.0.1',password='123456')
r=redis.Redis(connection_pool=pool)


def main():
    cmd="tail -f test.log"
    cmd=shlex.split(cmd)
    curr_day=datetime.date.today()
    process=subprocess.Popen(cmd,stdout=subprocess.PIPE)
    cnt = 'log'
    while True:
        line = process.stdout.readline()
        if line == '' and process.poll() is not None:
            break
        if line:
            print(line)
            r.lpush(curr_day,line)
            rc=process.poll()
        
main()