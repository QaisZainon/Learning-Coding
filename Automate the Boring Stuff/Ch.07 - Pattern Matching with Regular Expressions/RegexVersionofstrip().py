import re
def RegexStrip(a,b):
    charLeft = re.compile(r'^([%s]+)' % 'abc')
    charRight = re.compile(r'([%s]+$)' % 'abc')
    x = charLeft.sub(a, charRight.sub(a,b))
    print(x)

RegexStrip('',"aaabcfdsfsabca")