import string


def encode_charimage(charimg):
    charimg_lines = charimg.split("\n")
    encoded_lines = []
    for line in charimg_lines:
        if len(line) == 0:
            continue
        encoded_line = ""
        cursor = 0
        for index, char in enumerate(line):
            if index == 0:
                continue
            if index == len(line) - 1 and line[cursor] == char:
                encoded_line += "%s%s" % (line[cursor], index - cursor + 1)
                continue
            if char == line[cursor]:
                continue
            else:
                encoded_line += "%s%s" % (line[cursor], index - cursor)
                cursor = index
                if index == len(line) - 1:
                    encoded_line += "%s1" % line[cursor]
        encoded_lines.append(encoded_line)
    return "n".join(encoded_lines)


def decode_charimage(encoded_img, verbose=False):
    encoded_lines = encoded_img.split("n")
    lines = []
    for encoded_line in encoded_lines:
        parts = []
        is_digital = False
        cursor = 0
        for index, char in enumerate(encoded_line):
            char_is_digit = char in string.digits
            if index == 0:
                is_digital = char_is_digit
                continue
            if index == len(encoded_line) - 1 and char_is_digit == is_digital:
                parts.append(encoded_line[cursor:])
                continue
            if is_digital == char_is_digit:
                continue
            else:
                parts.append(encoded_line[cursor: index])
                cursor = index
                is_digital = not is_digital
                if index == len(encoded_line) - 1:
                    parts.append(char)
        if verbose:
            print parts
        line = ""
        step_cnt = len(parts) / 2
        for i in range(step_cnt):
            if verbose:
                print parts[i * 2: i * 2 + 2]
            line += parts[i * 2] * int(parts[i * 2 + 1])
        if verbose:
            print line
        lines.append(line)
    return "\n".join(lines)
