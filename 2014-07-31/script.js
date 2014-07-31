document.writeln('<pre>');

assert('LengthNotPositive', 'foo', 0, null);

assert('Empty', '', 1, '');
assert('OneWord', 'Hello', 10, 'Hello');

assert('BreakLongWordOnce', 'ab', 1, 'a\nb');
assert('BreakLongWordTwice', 'abc', 1, 'a\nb\nc');
assert('BreakTooLongWord', 'Superkalifragelistichexpialigetisch', 10, 'Superkalif\nragelistic\nhexpialige\ntisch');

assert('WrapTwoWords', 'a b', 1, 'a\nb');
assert('WrapTwoWordsWithSpaceAtBreak', 'a b', 2, 'a\nb');
assert('DontBreakWordsButWrapLines', 'abc def', 5, 'abc\ndef');

assert('Trivial wrap at new line', 'a\nb', 1, 'a\nb');
assert('Wrap at line break', 'abc\ndef', 5, 'abc\ndef');

assert('Keep line breaks', 'a\nb', 5, 'a\nb');
assert('Keep double line breaks', 'a\n\nb', 5, 'a\n\nb');

assert('Long text', 'This is a pretty longlonglong text let us see how this is  wrapped', 20,
    'This is a pretty\nlonglonglong text\nlet us see how this\nis  wrapped');

document.writeln('</pre>');

function assert(name, text, lineLength, expected) {
    var actual = wordWrap(text, lineLength);
    if (actual == expected) {
        document.writeln('.');
    } else {
        document.writeln(name + ' FAILED ' + encodeURI(actual));
    }
}

function wordWrap(text, lineLength) {
    if (lineLength < 1) {
        return null;
    }

    text = text.trim();
    if (text.length <= lineLength) {
        return text;
    }

    // find space before lineLength in text
    var lineEnd = text.substring(0, lineLength).replace('\n', ' ').lastIndexOf(' ');
    if (lineEnd == -1) {
        lineEnd = lineLength;
    }

    return text.substring(0, lineEnd).trim() + '\n' + wordWrap(text.substring(lineEnd), lineLength);
}