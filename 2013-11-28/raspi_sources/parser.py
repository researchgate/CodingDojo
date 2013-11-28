def parse(patterns):
        parsed = []
	count = 0
        for line in patterns.strip().split('\n'):
		count = count + 1
                (time, pattern) = line.split('-')
                delay = float(time)/1000
                if len(pattern) != 16:
                        raise Exception("Line " + str(count) + ": Wrong length")
                parsedPattern = ''
                for i in range(len(pattern)):
                        if int(pattern[i]) == 0:
                                parsedPattern = parsedPattern + ' '
                        else:
                                parsedPattern = parsedPattern + 'O'
                parsed.append((delay, parsedPattern))
        return parsed
