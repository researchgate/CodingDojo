__author__ = 'Team-DragOn (Vincenz and Michael)'

def matches(pattern, input):
    return matchesRec(pattern, input, 0, 0)

def matchesRec(pattern, input, patternIndex, inputIndex):
    if patternIndex == len(pattern) and inputIndex == len(input):
        return True

    if patternIndex < len(pattern):
        pChar = pattern[patternIndex]
        nextPCharStar = (patternIndex < len(pattern) - 1) and pattern[patternIndex + 1] == '*'

        if nextPCharStar and matchesRec(pattern, input, patternIndex + 2, inputIndex):
            return True

        if inputIndex < len(input):
            iChar = input[inputIndex]
            if nextPCharStar:
                return (pChar == iChar or pChar == '.') and matchesRec(pattern, input, patternIndex, inputIndex+1)

            if pChar == iChar or pChar == '.':
                return matchesRec(pattern, input, patternIndex+1, inputIndex+1)

    return False
