import subprocess as sp
import re


def is_connected():
    pattern = re.compile("([0-9A-F]{2}[:-]){5}([0-9A-F]{2})")
    out = sp.check_output(["hcitool", "con"])
    return pattern.match(out)
