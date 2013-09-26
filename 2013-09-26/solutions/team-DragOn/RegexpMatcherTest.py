__author__ = 'Team-DragOn (Vincenz and Michael)'

import RegexpMatcher

assert RegexpMatcher.matches('', '')

assert RegexpMatcher.matches('hello', 'hello')

assert not RegexpMatcher.matches('a', 'b')

assert not RegexpMatcher.matches('a', 'aa')

assert RegexpMatcher.matches('hel.o', 'helto')

assert RegexpMatcher.matches('hel*o', 'hello')

assert RegexpMatcher.matches('hel*o', 'hellllo')

assert RegexpMatcher.matches('hel*', 'hellll')

assert RegexpMatcher.matches('h.*', 'hell')

assert RegexpMatcher.matches('ab*b', 'abb')

assert RegexpMatcher.matches('ab*b', 'ab')

assert RegexpMatcher.matches('h.*o', 'hello')


assert not RegexpMatcher.matches('h.*oo', 'hello')

assert not RegexpMatcher.matches('h.*o', 'hell')
