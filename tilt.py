# based on https://raw.githubusercontent.com/atlefren/pytilt/master/pytilt.py

import sys
import datetime

import bluetooth._bluetooth as bluez

import blescan

TILTS = {
    'a495bb10c5b14b44b5121370f02d74de': 'Red',
    'a495bb20c5b14b44b5121370f02d74de': 'Green',
    'a495bb30c5b14b44b5121370f02d74de': 'Black',
    'a495bb40c5b14b44b5121370f02d74de': 'Purple',
    'a495bb50c5b14b44b5121370f02d74de': 'Orange',
    'a495bb60c5b14b44b5121370f02d74de': 'Blue',
    'a495bb70c5b14b44b5121370f02d74de': 'Yellow',
    'a495bb80c5b14b44b5121370f02d74de': 'Pink',
}

class Tilt:

    def __init__(self, uuid, color, timestamp, temp, gravity):
        self.uuid = uuid
        self.color = color
        self.timestamp = timestamp
        self.temp = temp
        self.gravity = gravity


def distinct(objects):
    seen = set()
    unique = []
    for obj in objects:
        if obj['uuid'] not in seen:
            unique.append(obj)
            seen.add(obj['uuid'])
    return unique


def to_celsius(fahrenheit):
    return round((fahrenheit - 32.0) / 1.8, 2)


def monitor_tilt():
    beacons = distinct(blescan.parse_events(sock, 10))
    results = []
    for beacon in beacons:
        if beacon['uuid'] in TILTS.keys():
            results.append(Tilt(
                beacon['uuid'],
                TILTS[beacon['uuid']],
                datetime.datetime.now().isoformat(),
                beacon['major'],
                beacon['minor']
            ))
    return results


def init(bt_id):
    try:
        sock = bluez.hci_open_dev(bt_id)
    except:
        print('error accessing bluetooth device...')
        sys.exit(1)
    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)


if __name__ == '__main__':
    dev_id = 0
    init(dev_id)
    results = monitor_tilt()
    for tilt in results:
        print("[{}] SG: {} Temp: {} @ {}".format(tilt.color, tilt.gravity, tilt.temp, tilt.timestamp))
