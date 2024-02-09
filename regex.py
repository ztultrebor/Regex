def match(pattern, text, result=''):
    """ String String -> Maybe String
        a Reg Exp that returns the first, simplest portion of text that matches pattern"""
    if pattern == '':
        return result
    elif text == '':
        return False
    elif len(pattern) > 2 and pattern[1] in ('*', '?'):
        return match_star(pattern[0], pattern[1], pattern[2:], text, result)
    elif len(pattern) == 2 and pattern[1] in ('*', '?'):
        return match_star(pattern[0], pattern[1], '', text, result)
    elif pattern[0] == text[0]:
        return match(pattern[1:], text[1:], result+text[0])
    else:
        return False
        

def match_star(p, op, pattern, text, result):
    """ String String -> Maybe String
        a Reg Exp that finds matches where '*' is involved"""
    yikes = match(pattern, text, result)
    if len(pattern) > 0 and yikes:
        return yikes
    elif op == '*' and p == text[0]:
        return match_star(p, op, pattern, text[1:], result+text[0])
    elif op == '?' and p == text[0]:
        return match(pattern, text[1:], result+text[0])
    else:
        return yikes


def tests():
    assert (match("s*ha", "ssssssshark!")) == "sssssssha"
    assert (match("s*ssha", "ssssssshark!")) == "sssssssha"
    assert (match("s*ha", "sssshhark!")) == False
    assert (match("s*ha", "hark!")) == "ha"
    assert (match("s*", "shark!")) == "s"
    assert (match("ps*", "pshark!")) == "ps"
    assert (match("ps*", "phark!")) == "p"
    assert (match("s?ssha", "ssssssshark!")) == False
    assert (match("s?ssha", "ssshark!")) == "sssha"
    assert (match("s?ssha", "sshark!")) == "ssha"
    assert (match("ps?", "pshark!")) == "ps"
    assert (match("ps?", "phark!")) == "p"
    print("Tests pass!")

tests()