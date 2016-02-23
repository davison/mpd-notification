# mpd-notification

A simple send/receive pair of daemons to co-ordinate around an mpd http stream

## mpd-notifier

A python service that polls a local (or remote, but that would seem odd) mpd
for its playing status.  If it is playing, it broadcasts that mpd's IP address
to a known multicast group to inform potential stream clients that play is
in progress.

## mpd-receiver

Another trivial python service that listens for the multicast packet and
invokes a local cvlc to start playing from the http stream.

The main purpose of this was to run it on an embedded device so I would expect
that you would need to run pulse audio (if that's your poison) in system mode
to make this work.  Alternatively, amend the .service file and add a line
`User=john` before deploying it.

## Installation

    # notifier
    sudo ./install.sh n

    # receiver
    sudo ./install.sh r

