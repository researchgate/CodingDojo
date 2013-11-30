import httplib, urllib, sys, Tkinter as tk, random

applePos = 6
headPos = 0
direction = "Right"
cycle = 0

period = 100
cycles = 10

def send(delay, pattern):
	# conn = httplib.HTTPConnection("192.168.178.134:8080")
	# conn.request("POST", "/", str(delay) + "-" + pattern)
	# response = conn.getresponse()
	# data = response.read()
	# conn.close()
	localConn = httplib.HTTPConnection("localhost:8080")
	localConn.request("POST", "/", str(delay) + "-" + pattern)
	response = localConn.getresponse()
	data = response.read()
	localConn.close()
	print data
	
def onKeyPress(event):
	global direction
	if event.keysym == "Down" and direction != "Up" \
			or event.keysym == "Up" and direction != "Down" \
			or event.keysym == "Left" and direction != "Right" \
			or event.keysym == "Right" and direction != "Left":
		direction = event.keysym
		
def moveSnake():
	global headPos, direction, applePos, cycle
	
	cycle = cycle + 1
	
	if cycle % cycles != 0:
		updateSnakeHead(headPos)
		root.after(period, moveSnake)
		return
	
	print direction
	
	row = headPos / 4
	col = headPos % 4
	
	if direction == "Up":
		row = row - 1
	elif direction == "Right":
		col = col + 1
	elif direction == "Down":
		row = row + 1
	else:
		col = col - 1
		
	if row < 0 or row > 3 or col < 0 or col > 3:
		print "COLLISION!!"
		send(1000, "1111111111111111")
		root.after(1000, start)
	else:
		headPos = row * 4 + col
		if headPos == applePos:
			applePos = random.randint(0,15)
		updateSnakeHead(headPos)
		root.after(period, moveSnake)

def updateSnakeHead(pos):
	if cycle % 2 == 0:
		apple = '0'
	else:
		apple = '1'
		
	pattern = "0000000000000000"
	pattern = pattern[0:pos] + "1" + pattern[pos+1:]
	pattern = pattern[0:applePos] + apple + pattern[applePos+1:]
	print pos
	send(100, pattern)
	
def start():
	global headPos, direction
	headPos = 0
	direction = 'Right'
	updateSnakeHead(0)
	root.after(period, moveSnake)

root = tk.Tk()
root.bind('<KeyPress>', onKeyPress)
start()
root.mainloop()
