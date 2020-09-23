import re

#Open MadLibs File
MadLibs = open('C:\\Users\\Dr. Wan Asna\\Desktop\\Python Projects\\Automate the Boring Stuff\\Ch.09 - Reading and Writing Files\\MadLibs.txt')
#Save contents so you can modify it
content = MadLibs.read()
MadLibs.close()
Regex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
#Loop to check for the words to replace it
#.search() only returns the first match it finds 
while True:
    result = Regex.search(content)
#end the loop if there is nothing left to replace
    if result == None:
        break
#Get user input as soon as one is found(if statement coulhdv been done better)
    if result.group() == 'ADJECTIVE' or result.group() == 'ADVERB':
        print('Enter an %s:' % (result.group().lower()))
    elif result.group() == 'NOUN' or result.group() == 'VERB':
        print('Enter a %s:' % (result.group().lower()))
    i = input()
#substitute the word as soon as you come across it
#the integer sets a limit on how many words it needs to substitute
    content = Regex.sub(i, content, 1) 
print(content)
MadLibs = open('C:\\Users\\Dr. Wan Asna\\Desktop\\Python Projects\\Automate the Boring Stuff\\Chapter 9 - Reading and Writing Files\\MadLibs.txt','w')
MadLibs.write(content)

