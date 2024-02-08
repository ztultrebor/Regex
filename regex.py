def match(pattern, text, result=''):
    """ String String -> Maybe String
    a Reg Exp that finds matches where '*' is involved"""
    if pattern == '':
        return result
    elif text == '':
        return False
    yattern = pattern + '  '
    p, op, attern = yattern[0], yattern[1], yattern[2:]
    if op == '*':
        yikes = match(attern[1:-2], text[1:], result+text[0])
        if attern[0] == text[0] and yikes:
            return yikes
        else:
            yikes = match(pattern, text[1:], result+text[0])
            if p[0] == text[0] and yikes:
                return yikes
            else: 
                return match(attern[:-2], text, result)
    else:
        yikes = match(pattern[1:], text[1:], result+text[0])
        if pattern[0] == text[0] and yikes:
            return yikes
        else: 
            return False



def tests():
    assert (match("s*ha", "ssssssshark!")) == "sssssssha"
    assert (match("s*ssha", "ssssssshark!")) == "sssssssha"
    assert (match("s*ha", "sssshhark!")) == False
    assert (match("s*ha", "hark!")) == "ha"
    assert (match("s*", "shark!")) == "s"
    assert (match("ps*", "pshark!")) == "ps"
    print("Tests pass!")

tests()
