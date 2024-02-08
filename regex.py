def match(pattern, text, result=''):
    if pattern == '':
        return True
    yattern = pattern + '  '
    p, op, attern = yattern[0], yattern[1], yattern[2:]
    if op == '*':
        if attern[0] == text[0] and (len(attern)==3 or match(attern[1:-2], text[1:])):
            return True
        elif p[0] == text[0] and match(pattern, text[1:]):
            return True
        else: 
            return match(attern[:-2], text)
    else:
        if pattern[0] == text[0] and (len(pattern)==1 or match(pattern[1:], text[1:])):
            return True
        else: 
            return False

def tests():
    assert (match("s*ha", "ssssssshark!")) == True
    assert (match("s*ssha", "ssssssshark!")) == True
    assert (match("s*ha", "sssshhark!")) == False
    assert (match("s*ha", "hark!")) == True
    assert (match("s*", "shark!")) == True
    print("Tests pass!")

tests()
