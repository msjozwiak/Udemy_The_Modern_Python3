import re

"""EX1 _time_validating"""


def is_valid_time(input_time):
    time_pattern = re.compile(r'^\d\d?:\d{2}$')
    mach = time_pattern.search(input_time)
    if mach:
        return True
    else:
        return False


# print(is_valid_time("10:50"))
# print(is_valid_time("1:70"))
# print(is_valid_time("9999"))
# print(is_valid_time("it is 9999"))


""""EX2 parsing_bytes_exercise"""


def parse_bytes(my_input):
    bytes_regex = re.compile(r"\b[10]{8}\b")
    mach = bytes_regex.findall(my_input)
    return mach


# print(parse_bytes("10101001"))


"""EX3 date_parsing_exercise"""


def parse_date(date_input):
    date_regex = re.compile(r"^([0-3][1-9])[.,/]([0-1][0-9])[.,/]([1-2][0-9]{3})$")
    mach = date_regex.search(date_input)
    if mach:
        return {"d": mach.group(1), "m":  mach.group(2),  "y": mach.group(3)}
    else:
        return None


# print(parse_date("12,04,2003"))


"""EX4 regex profanity filter"""


def censor(text_input):
    pattern = re.compile(r'\bfrack[a-z]*\b', re.IGNORECASE)
    result = pattern.sub("CENSORED", text_input)
    print(result)

# censor("Frack you")
# censor("I hope you fracking die")
# censor("You fracking Frack")
