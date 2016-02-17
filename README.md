# mpd-notification
A simple send/receive pair of daemons to co-ordinate around an mpd http stream

## mpd-poller
A python service that polls a local (or remote, but that would seem odd) mpd for its playing status.  If it is playing, it broadcasts that mpd's IP address to a known multicast group to inform potential stream clients that play is in progress

## mpd-listener
A second trivial python service that listens for the multicast packet and invokes a local cvlc to start playing from the http stream.
