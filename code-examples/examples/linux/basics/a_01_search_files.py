
#-#-#-#-#

#s 1: #Login
#a: Login
#c: show-line: {1:1}
w
#-#-#-#-#


#s 1: #Search files
#a: Search files
#s 2: List all files and folders in current folder
#a: To list all files and folders in current folder, use ls, which stands for list:
#c: show-line: {1:1}
ls
#-#-#-#-#


#s 1: #List with option
#a: List with option
#s 2: -a for all, -l for long listing, -la combined
#a: List all files and folders with option -a to also show hidden files, -l for long listing or combine both with -la
#c: show-line: {1:1}
ls -la
#-#-#-#-#

#s 1: #Find
#a: Find
#s 2: Find a file in a folder or in all sub-folders
#a: To find a file in a specific folder or in all its sub-folders use the find method. For example, to find all files called cat.png in the folder etc, use:
#c: show-line: {1:1}
find /etc/ -name cat.png
#-#-#-#-#

#s 1: #Find case insensitive
#a: Find case insensitive
#s 2: Find a file, independent if the letters are written in upper or lower case
#a: To find a file independent of if the letters of the file name are written in upper or in lower case, use the option -iname:
#c: show-line: {1:1}
find /etc/ -iname cat.png
#-#-#-#-#

#s 1: #Find specific file type
#a: Find specific file type
#s 2: Find all files of a specific type
#a: To find all files of a specific type, use the star symbol as a placeholder. For example, to find all text files, use:
#c: show-line: {1:1}
find /etc/ -name "*.text"
#-#-#-#-#

#s 1: #Redirect of output
#a: Redirect of output
#s 2: Redirect text to file
#a: To redirect a console output, use the symbol greater than. For example, to redirect the text Hello into a file called test.txt use:
#c: show-line: {1:1}
echo "Hello" > test.txt
#-#-#-#-#


#s 1: #Touch
#a: Touch
#s 2: Usages: create new file if not present, or change timestampt if present
#a: The touch command has two use cases. If the file is already present, then touch changes the timestamp of the file. If there is no file with the specified name, then touch generated an empty file. For example, to generate a new empty file with the name test.txt, use:
#c: show-line: {1:1}
touch test.txt
#-#-#-#-#


#s 1: #Cat
#a: Cat
#s 2: Shows the content of a file
#a: To show the content of a file, the cat command can be used. For example, to see the content of the file test.txt use:
#c: show-line: {1:1}
cat test.txt
#-#-#-#-#


#s 1: #Copy a file
#a: Copy a file
#s 2: Copy a file from one folder another
#a: To copy a file from one folder to another, use the cp command. For example, to copy the file test.txt from the current location to the folder etc, use:
#c: show-line: {1:1}
cp test.txt /etc
#-#-#-#-#
