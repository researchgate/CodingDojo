# Nikolas Martens (rtens.org) - 2013-09-26

# Here are my test cases. I'm sure there is something I missed ;)
def test():
    assert matches('','')
    assert matches('', 'a')
    assert not matches('b', 'a')
    assert matches('a', 'aa')
    assert matches('b', 'abc')
    
    assert matches('.', 'a')
    assert matches('a.c', 'abc')
    assert matches('.c', 'abc')
    assert not matches('.c', 'abd')
    
    assert matches('a*', 'a')
    assert matches('a*', 'aa')
    assert matches('a*', 'aaa')
    assert matches('ba*', 'baaa')
    
    assert matches('a*', '')
    assert matches('ba*', 'b')
    assert matches('ba*', 'bc')
    
    assert matches('.*', '')
    assert matches('.*', 'aaaa')
    assert matches('.*.', 'aaaa')
    assert matches('.*.', 'a')
    assert not matches('.*.', '')
    assert matches('a.*c', 'abc')
    assert matches('a.*c', 'abbbc')
    
    assert matches('ba*a', 'ba')
    assert matches('ba*aa', 'baaa')
    assert matches('b.*aa', 'baaa')
    
    assert matches('^abc', 'abc')
    assert not matches('^bc', 'abc')
    assert matches('bc$', 'abc')
    assert not matches('ab$', 'abc')
        

# And this was my first solution. It covers all cases until line 31 but doesn't lend itself nicely
# to the whole backtracing issue. So I decided a new approach.

def matches_old(pattern, string):
    p = 0
    s = 0
    repeat = ''
    
    while p < len(pattern):
        if repeat != '':
            if s >= len(string) or string[s] != repeat:
                repeat = ''
            else:
                p -= 1
        elif p+1 < len(pattern) and pattern[p+1] == '*':    
            s -= 1
            repeat = pattern[p]
        elif s >= len(string):
            return False
        elif pattern[p] == '.':
            pass
        elif string[s] != pattern[p]:
            p -= 1
            
        s += 1
        p += 1
    return True

# This second approach uses recursion. This lets me nicely try out repitions in a non-greedy
# fashion and backtrace easily.

def matches(pattern, string, anchored = False):
    if pattern == '':
        return True
    
    if len(pattern) > 1 and pattern[1] == '*':
        for s in range(0, len(string)+1):
            if matches(pattern[2:], string[s:], True):
                return True
        
    if pattern[0] == '$':
        return string == ''
    elif string == '':
        return False
    elif pattern[0] == '^':
        return matches(pattern[1:], string, True)
    elif pattern[0] == '.' or pattern[0] == string[0]:
        return matches(pattern[1:], string[1:])
    elif not anchored:
        return matches(pattern, string[1:])
    else:
        return False


if __name__ == '__main__':
    test()
    print 'OK'