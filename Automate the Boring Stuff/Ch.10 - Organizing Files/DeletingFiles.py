#Risky code as might accidently delete important files
import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):
    #wrong filename to be deleted
    os.unlink(filename)

#Try this as the delete function is commented, and the filename is printed for checking purposes
import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):
    #os.unlink(filename)
    print(filename)
#Once you're certain about the filename, delete the # and run the program to delete the files
