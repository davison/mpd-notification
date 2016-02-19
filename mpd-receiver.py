#!/usr/bin/env python

import socket
import struct
import subprocess
import sys

MCAST_GRP = '224.1.2.3'
MCAST_PORT = 5007


while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((MCAST_GRP, MCAST_PORT))
        mreq = struct.pack('4sl', socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        mpd_host = sock.recv(10240)
        sock.close()
        subprocess.call(["/usr/bin/cvlc", "http://" + mpd_host + ":8000", "--play-and-exit", "-q"])
    
    except socket.error as err:
        print (err[1])
        sys.exit()


