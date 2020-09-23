spam = ['apples','bananas','tofu','cats']
spam1 = ['red','blue','orange','purple','green','black']
spam2 = []

def sort(sorty):
    if sorty != []:
        for i in range(0,(len(sorty)-1)):
            print(sorty[i] + ', ' ,end ='')
        print( 'and ' + sorty[len(sorty)-1])
    else:
        print('You did not put any lists')

sort(spam)
               
