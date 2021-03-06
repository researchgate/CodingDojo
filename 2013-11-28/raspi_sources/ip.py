patterns = {\
'0' : 	'0110' + \
	'1001' + \
	'1001' + \
	'0110',

'1' :   '0010' + \
        '0110' + \
        '0010' + \
        '0010',

'2' :   '0110' + \
        '1001' + \
        '0010' + \
        '1111',

'3' :   '1111' + \
        '0001' + \
        '0011' + \
        '1111',

'4' :   '1000' + \
        '1010' + \
        '1111' + \
        '0010',

'5' :   '1111' + \
        '1100' + \
        '0001' + \
        '1111',

'6' :   '0111' + \
        '1000' + \
        '1111' + \
        '1111',

'7' :   '1111' + \
        '0001' + \
        '0010' + \
        '0010',

'8' :   '0111' + \
        '0111' + \
        '0101' + \
        '0111',

'9' :   '0111' + \
        '0111' + \
        '0001' + \
        '0111',

'.' :   '0000' + \
        '0000' + \
        '0000' + \
        '0010',

' ' :   '0000' + \
        '0000' + \
        '0000' + \
        '0000',
}

import sys

ip = sys.argv[1]

f = open('pattern', 'w')

for c in ip:
	f.write('1000-' + patterns[c] + "\n")
	f.write('50-' + patterns[' '] + "\n")

f.close()
