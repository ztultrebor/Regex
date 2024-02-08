def match(pattern, text):
    p, op, attern = pattern[0], (pattern+' ')[1], (pattern+'  ')[2:]
    if op == '*':
        if attern[0] == text[0] and (len(attern)==1 or match(attern[1:-2], text[1:])):
            return True
        elif p[0] == text[0] and match(pattern, text[1:]):
            return True
        else: 
            return False
    else:
        if pattern[0] == text[0] and (len(pattern)==1 or match(pattern[1:], text[1:])):
            return True
        else: 
            return False


print(match("s*ha", "ssssssshark!"))
