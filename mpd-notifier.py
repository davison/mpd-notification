#!/usr/bin/env python

import socket
import mpd
import time
import os

# TODO: make configurable
MCAST_GRP = '224.1.2.3'
MCAST_PORT = 5007
mpd_port = int(os.environ.get('MPD_PORT', 6600))
mpd_host = os.environ.get('MPD_HOST', 'localhost')

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    mpc = mpd.MPDClient()
    mpc.connect(mpd_host, mpd_port)

    while True:
        status = mpc.status()['state']
        if status == 'play':
            sock.sendto(mpd_host, (MCAST_GRP, MCAST_PORT))
        time.sleep(10)
    sock.close()

except socket.error as err:
    print (err[1])
    sys.exit()

