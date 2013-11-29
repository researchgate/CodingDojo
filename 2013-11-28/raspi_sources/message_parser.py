import symbols


def parse(input_message):
    lines = [
        '0000',
        '0000',
        '0000',
        '0000'
    ]

    input_message += "$"

    for char in list(input_message):
        char = char.upper()
        if not char in symbols.chars:
            continue

        lines[0] += symbols.chars[char][0] + '0'
        lines[1] += symbols.chars[char][1] + '0'
        lines[2] += symbols.chars[char][2] + '0'
        lines[3] += symbols.chars[char][3] + '0'

    messages = []
    for index in range(0, len(lines[0]) - 5):
        message = lines[0][index:index+4]
        message += lines[1][index:index+4]
        message += lines[2][index:index+4]
        message += lines[3][index:index+4]
        messages.append(message)

    delay = 250
    return '\n'.join(map(lambda x: str(delay) + "-" + str(x), messages))