import RPi.GPIO as io
import time
import parser

io.setmode(io.BOARD)

pins = [3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24]

for i in pins:
	io.setup(i, io.OUT)
	io.output(i, False)

while False:
	for i in pins:
		io.output(i, True)
		time.sleep(0.2)
		io.output(i, False)

while True:
	f = open('pattern')
	content = f.read()
	f.close()

	if content.strip() == '':
		continue

	patterns = parser.parse(content)
	
	for delay, pattern in patterns:
		for p in range(len(pattern)):
			io.output(pins[p], pattern[p] != ' ')
		time.sleep(delay)
