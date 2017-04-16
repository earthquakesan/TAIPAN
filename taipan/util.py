"""Utils"""
import numpy
import os
import re
from dateutil.parser import parse

def load_csv(csvPath):
    """Load CSV file to numpy array"""
    if(os.path.exists(csvPath) and os.stat(csvPath).st_size):
        csv_bytes = numpy.genfromtxt(
            csvPath,
            delimiter=",",
            dtype="S",
            comments="///",
            missing_values="NULL",
            invalid_raise=False
        )
        csv = csv_bytes.view(numpy.chararray).decode("utf-8")
        if numpy.shape(csv) != (0,):
            for x in numpy.nditer(csv, op_flags=['readwrite']):
                x[...] = x.flatten()[0].strip('"')
            return csv
        else:
            return []
    else:
        return []

def clear_string(string):
    string = re.sub('[{}|*?()\[\]!-"]', '', string)
    string = re.sub('&nbsp;', '', string)
    string = string.strip()
    return string

class DateRecognizer(object):
    def __init__(self):
        float_digit_pattern = re.compile("-?\d+\.\d+")
        one_digit_pattern = re.compile("^-?\$?\d+$")
        nbsp_digit_pattern = re.compile("^&nbsp;\d+$")
        pg13_pattern = re.compile("PG-13")
        ps3_pattern = re.compile("^ps3$")
        currency_pattern = re.compile(".*illion.*")
        one_thousand_pattern = re.compile("^10\d+")
        aplusb_pattern = re.compile("^\d+\+\d+")
        aminusb_pattern = re.compile("^\d+-\d+")
        self.skip_patterns = [
            float_digit_pattern, one_digit_pattern, pg13_pattern, currency_pattern, nbsp_digit_pattern, ps3_pattern, one_thousand_pattern, aplusb_pattern, aminusb_pattern
        ]

    def is_date(self, string):
        parsedTime = ""

        for pattern in self.skip_patterns:
            if(pattern.match(string)):
                return False

        try:
            parsedTime = parse(string, fuzzy=True)
        except BaseException as e:
            return False

        try:
            if(parsedTime == parse("", fuzzy=True)):
                return False
            else:
                return True
        except:
            return True