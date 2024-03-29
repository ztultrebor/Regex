
#=====================
# functions


def match(pattern, text, result=''):
    """ String String String -> Maybe String
        a Reg Exp that returns the first, greedy match"""
    lp = len(pattern)
    if lp == 0:
        return result
    elif text == '':
        return False
    elif lp > 1 and pattern[1] == '*':
            return match_star(pattern[0], pattern[2:], text, result)
    elif lp > 1 and pattern[1] == '?':
            return match_perhaps(pattern[0], pattern[2:], text, result)
    elif lp > 1 and pattern[1] == '+':
            return match_plus(pattern[0], pattern[2:], text, result)
    elif pattern[0] == text[0]:
        return match(pattern[1:], text[1:], result+text[0])
    else:
        return False
        

def match_star(p, pattern, text, result):
    """ String String String String -> Maybe String
        a Reg Exp that finds matches where '*' is involved"""
    yikes = match(pattern, text, result) # if you can match without using p, do so
    if len(pattern) > 0 and yikes:
        return yikes
    elif p == text[0]:
        return match_star(p, pattern, text[1:], result+text[0])
    else:
        return yikes
    

def match_perhaps(p, pattern, text, result):
    """ String String String String -> Maybe String
        a Reg Exp that finds matches where '?' is involved"""
    yikes = match(pattern, text, result) # if you can match without using p, do so
    if len(pattern) > 0 and yikes:
        return yikes
    elif p == text[0]:
        return match(pattern, text[1:], result+text[0])
    else:
        return yikes


def match_plus(p, pattern, text, result):
    """ String String String String -> Maybe String
        a Reg Exp that finds matches where '+' is involved"""
    if p == text[0]:
        return match_star(p, pattern, text[1:], result+text[0])
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