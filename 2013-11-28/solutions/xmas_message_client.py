import requests
import sys

if len(sys.argv) < 3:
    print "Usage:"
    print sys.argv[0] + " \"<server-url>\" \"<message>\" [<verbose>]"
    print "Example:"
    print sys.argv[0] + " \"http://localhost:8080\" \"hello world\" 1"
    exit()

url = sys.argv[1]
inputMessage = sys.argv[2]
verbose = False

if len(sys.argv) > 3:
    verbose = True

chars = {
    "A":[
        "0110",
        "1001",
        "1111",
        "1001"
    ],
    "B": [
        "100",
        "111",
        "101",
        "111"
    ],
    "C": [
        "011",
        "100",
        "100",
        "011"
    ],
    "D": [
        "1110",
        "1001",
        "1001",
        "1110"
    ],
    "E": [
        "1111",
        "1110",
        "1000",
        "1110"
    ],
    "F": [
        "1111",
        "1110",
        "1000",
        "1000"
    ],
    "G": [
        "1111",
        "1000",
        "1001",
        "1111"
    ],
    "H": [
        "1001",
        "1111",
        "1001",
        "1001"
    ],
    "I": [
        "1",
        "1",
        "1",
        "1"
    ],
    "J": [
        "111",
        "001",
        "101",
        "111"
    ],
    "K": [
        "1010",
        "1100",
        "1010",
        "1001"
    ],
    "L": [
        "1000",
        "1000",
        "1000",
        "1111"
    ],
    "M": [
        "10001",
        "11011",
        "10101",
        "10001"
    ],
    "N": [
        "1001",
        "1101",
        "1011",
        "1001"
    ],
    "O": [
        "1111",
        "1001",
        "1001",
        "1111"
    ],
    "P": [
        "1110",
        "1001",
        "1110",
        "1000"
    ],
    "Q": [
        "11110",
        "10010",
        "11110",
        "00001"
    ],
    "R": [
        "1110",
        "1001",
        "1110",
        "1010"
    ],
    "S": [
        "0111",
        "1100",
        "0011",
        "1110"
    ],
    "T": [
        "11111",
        "00100",
        "00100",
        "00100"
    ],
    "U": [
        "1001",
        "1001",
        "1001",
        "1111"
    ],
    "V": [
        "1000001",
        "0100010",
        "0010100",
        "0001000"
    ],
    "W": [
        "10001",
        "10001",
        "10101",
        "01110"
    ],
    "X": [
        "01010",
        "00100",
        "01010",
        "10001"
    ],
    "Y": [
        "10001",
        "01010",
        "00100",
        "00100"
    ],
    "Z": [
        "1111",
        "0010",
        "0100",
        "1111"
    ],
    " ": [
        "00",
        "00",
        "00",
        "00"
    ],
    "$": [
        "00000",
        "00000",
        "00000",
        "00000"
    ],
}

def sendPattern(delay, patterns, debug):
    message = '\n'.join(map(lambda x: str(delay) + "-" + str(x), patterns))
    if debug:
        print(message)
    r = requests.post(url, message)
    print(r.text)

lines = [
    '',
    '',
    '',
    ''
]

inputMessage += "$"

for char in list(inputMessage):
    char = char.upper()
    if not char in chars:
        continue

    lines[0] += chars[char][0] + '0'
    lines[1] += chars[char][1] + '0'
    lines[2] += chars[char][2] + '0'
    lines[3] += chars[char][3] + '0'

messages = []
for index in range(0, len(lines[0]) - 5):
    message = lines[0][index:index+4]
    message += lines[1][index:index+4]
    message += lines[2][index:index+4]
    message += lines[3][index:index+4]
    messages.append(message)

sendPattern(300, messages, verbose)