from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from luma.core.virtual import viewport, snapshot
from datetime import datetime
import time
import ip
import bluetooth
import last_line

serial = i2c(port=1, address=0x3c)
device = ssd1306(serial, rotate=0)


def bt_is_connected(draw, pos=(1, 0)):
    is_conn = bluetooth.is_connected()
    out = "B+" if is_conn else "b-"
    draw.text(pos, out, fill="white")


def wifi_is_connected(connected, draw, pos=(16, 0)):
    out = "W+" if connected else "w-"
    draw.text(pos, out, fill="white")


def ip_address(address, draw, pos=(1, 40)):
    out = address if address else "Not Connected"
    draw.text(pos, out, fill="white")


def last_result(out, draw, pos=(1, 15)):
    draw.text(pos, out, fill="white")


def last_result_render():
    row = last_line.last()[0]
    format = '%H:%M'
    dt = datetime.strftime(row['date'], format) if row else datetime.now().strftime(format)
    out = "{color}: {gravity} @ {datetime}".format(color=row['color'], gravity=row['gravity'],
                                                   datetime=dt) if row else "No results @ {}".format(dt)
    return out


def run():
    while 1:
        with canvas(device) as draw:
            bt_is_connected(draw)
            addr = ip.get_ip_address('wlan0')
            wifi_is_connected(addr, draw)
            last_result(last_result_render(), draw)
            ip_address(addr, draw)
        time.sleep(20)


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        pass
