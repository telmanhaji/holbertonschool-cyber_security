#!/bin/bash
ps -u "$1" -o user,pid,pcpu,pmem,vsz,rss,stat,start,time,comm | grep -v "0      0"
