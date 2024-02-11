
#=====================
# functions


def match(pattern, text, result=''):
    """ String String -> Maybe String
        a Reg Exp that returns the first, simplest portion of text that matches pattern"""
    lp = len(pattern)
    if lp == 0:
        return result
    elif text == '':
        return False
    elif lp > 1 and pattern[1] in ('*', '?', '+'):
        if pattern[1] in ('*', '?'):
            return match_star(pattern[0], pattern[1], pattern[2:lp], text, result)
        elif pattern[1] == '+':
            return match_plus(pattern[0], pattern[1], pattern[2:lp], text, result)
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
    elif p == text[0]:
        if op == '*':
            return match_star(p, op, pattern, text[1:], result+text[0])
        else:
            return match(pattern, text[1:], result+text[0])
    else:
        return yikes
    

def match_plus(p, op, pattern, text, result):
    if op == '+' and p == text[0]:
        return match_star(p, '*', pattern, text[1:], result+text[0])
    else:
        False



#=====================
# tests


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
    assert (match("s+ssha", "ssssssshark!")) == "sssssssha"
    assert (match("s+ssha", "sssssssh")) == False
    print("Tests pass!")
tests()