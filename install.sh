#!/bin/bash
#
# pass a single parameter 'n' or 'r' to install either the (n)otifier or
# the (r)eceiver
#
# ----------------------------------------------------------------------------

function die {
    echo $1
    exit $2
}

function install {
    cp mpd-${1}.py /usr/bin/mpd-$1
    chmod +x /usr/bin/mpd-$1
    cp mpd-${1}.service /lib/systemd/system
    touch /etc/default/mpd-notification
    systemctl enable mpd-$1
    systemctl start mpd-$1
    systemctl status mpd-$1
}


# ----------------------------------------------------------------------------

[[ $EUID -eq 0 ]] || die "Must be run as root" 1
[[ "$1" == "n" || $1 == "r" ]] || die "Must pass 'n' or 'r' as first argument to install (n)otifier or (r)eceiver" 2

target=receiver
[[ "$1" == "n" ]] && target=notifier
install $target

exit 0

