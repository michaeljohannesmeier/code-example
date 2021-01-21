#-#-#-#


# Info about system
uname -a

# Get hostname of machine
hostname

# Get ip address
hostname -I


# List disk
fdisk /dev/sda -l
# first disk = a (sda), second = b (sdb), ...

# parted command -> interactive see disk settings
parted


# list all files and folders
echo *


# show which shell
echo $SHELL
vim /etc/passwd




## Venv
# list all env variables
env

# set new env variable
#current shell
hello="test"
# all new shells (persistently)
export env hello="test"

#unset variable (persistently)
unset hello




# start new shell
bash

# show file tree
apt-get install tree
# show tree
tree



## Ls
# ls with time
ls -lt
# ls reverse time
ls -lrt


## Cat
# start interactive file (end with ctrl+d)
cat > test.txt
#concatenate two files
cat test1.txt test2.txt > combined.txt

## Rm
# remove file
rm test.txt
# remove empty directory
rm directory
rmdir directory
# remove recursive force directory
rm -rf directory


# show history
cat /home/user/.bash_history


## cp
# file
cp test.txt test2.txt
# directory
cp -r test_folder 


# mv
# move file
mv test1.txt /root/
# rename
mv test1.txt test2.txt



# show loggged in users
who
# get username
whoami
# switch user
su - john
# show which file is executed for command
which tty


## date
# show date
date
# show date in utc
date -u
# show only time
date +"%T"
# show day
date +"%d"
# show date
date +"%F"
# custom format
date +"%m-%d-%Y"
# set a date (%m%d%H%M%Y.%S)
date 080215362017.37


## vim
# switch to insert mode
i
# switch to command mode
ESC
# delete a line 
dd
# delete 5 lines
5dd
# open new line
o
# delete a word
dw
# delete 3 words
3dw
# delete a character
x
# copy a line
yy
# paste
p
# undo
u
# show line number
:set nu
# search for test
/test
# next word
SHIFT+e
# go to line 1
:1
# go to end of file
SHIFT+g
# save file
:wq
# dont save
:q!
# show filename
:f
# vertical split
:vsp
# jumpt to other screen
STRG+ww
# next file
:bn


## permissions
# see permissions
ls -la
# - is file, d is directory, r is read, w = write, x = execute
# 4 = read, 2 = write, 1 = execute
# full permissions to user, group and others
chmod 777 test.txt
# add write to group
chmod g+w
# remove r from user
chmod u-r
# set permission
chmod u=rwx
# recursive to folder
chmod -R 777 test
# change group
chgrp mike test.txt
# change user and group recursively
chown -R john:john test.txt
# show all users
vim /etc/passwd
getent
# get all groups
vim /etc/group
getent group
# get id
id
# get user id (superuser uid = 0)
id -u



## Background jobs
# stop a job, is still there in the background
CTRL + Z
# see jobs
jobs
# continue to run job nr 1 in background mode
bg %1
# stop job
kill %1
# continue to run/bring job nr 1 in foreground
fg %1
# run in background
sh test.sh &

## Sort and unique
# sort content of file
sort test.txt
# sort numerical
sort -n test_numbers.txt
# reverse numerical
sort -rn test_numbers.txt
# sort multiple files, only unique values
sort -nu file1.txt file2.txt
# filter out non unique when adjasent to each other
cat test.txt | uniq


## Ps
# show current processes
ps -ef
# show processes with exact command
ps auxwww


# Redirects
# 0 stdin, 1 stdout, 2 stderr
# redirect to file or stdout with: >
ls -la > test.txt
# create empty file
> test.txt
# input from a file or stdin with: <
# >> append to a file
echo hello >> test.txt
# >> redirect and append to file
# redirect stdout to file
1 > test.txt
# redirect stderr to stdout and save stdout to file
ls -la /xxx > test.txt 2>&1
# append stdou to a file
1 >> test.txt
# redirect stderr to a file
2 > test.txt
# redirect stderr and stdout to a file
&> test.txt
# dev/null discards all content
ls -la /dev/null
# show status of last input
echo $?
# redirect file descriptor 3 to test.txt
exec 3<> test.txt
echo "hello" >&3
# close file descriptor 3
exec 3>&-

## Pipes
# page by page output
ls -lR | less
# top 10 rows
ls -lR | head -10
# find all files
find . -type f
# cound all files
find . -type f | wc
# cound only lines
find . -type f | wc -l
# write something to screen and also to stdout
echo "hello" | tee test.txt

## Wildcards
# ? = 1 character
# ??? = 3 characters
# * = everything
# list ony txt file
ls *.txt
# list man mbn
ls m[a-b]n
# list doc file and pdf files
ls {*.doc, *.pdf}
# exclude 9
ls *[!9]*

## Find
# find filename test.txt
find . -name test.txt
# find all files
find . -type f
# find case insensitive name
find . -iname test.txt
# find all txt files
find . -type f -iname "*.txt"
# only search in 2 sub folders
find . -name test.txt -maxdepth 2
# find all files which are not .txt files
find . -not -iname "*.txt"
# find all .txt or .sh files
find . -iname ".txt" -o -iname "*.sh"
# find with and
find . -iname ".txt" -a -iname "*test*"
# find file with name test but not .txt extension
find . -iname "test*" ! -iname ".txt"
# find directory with name test
find . -type d -name "test"
# find in two paths
find /paht1 /path2 -iname "test.txt"
# find all hidden files
find . -type f -name ".*"
# find file without wrx permissions
find . -type f ! -perm 0777
# find file with sticky permission for user
find . -type f -perm /u=s
# find file with only read permission for user
find . -type f -perm /u=r
# find files with execute permission for u, g and o
find . -type f -perm /a=x
# find all files of user john
find . -user john
# find files modified in last 10 days
find . -mtime 10
# find files accessed in last 5 days
find . -atime 5
# find files modified in greater 10 but less than 100 days
find . -mtime +10 -mtime -100
# find all files which have been changed in the last 10 minutes
find . -cmin 10
# find file with size of around 50 M
find . -size 50M
# find file size between 50M and 100M
find . -size +50M -size -100M
# find all empty files
find . -type f -empty
# find all empty directories
find . -type d -empty
# find and execute
find . -type f -exec ls -ld {} \;


## Grep
# search case insensitive "hello" in test.txt file (returns all the lines)
grep -i "hello" test.txt
# recursively search all files and folders everywhere
grep -r "hello" *
# all files which does not include hello case insensitive
grep -riv hello *
# count the number of occurrences
grep -c "hello" test.txt
# grep with extension -E
grep -E -w 'hello|welcome' test.txt
# only list column 3, sort and unique only
nm a.out | awk '{print $3}' | sort | uniq
# search for speed of ethernet
sudo ethtool enp0s8 | grep -i speed
# match exactly hello (helloa not matched)
grep -w hello test.txt
# search with line number
grep -in hello test.txt
# serach for proxy and doxy
grep [pd]oxy test.txt
# show 3 lines after and before pattern was found
grep -A 3 -B 3 hello test.txt 
# serach from a file
grep -f patterns.txt test.txt


############################
## Shell script
# argument 1
$1
# argument 2
$2
# all arguments in one string
$*
# all arguments in a list
$@
# devine/call function (dont have arguments)
printhello()
{
    echo "hello"
}
printhello
# run in debug
#!/bin/bash -x
# if statement
if [$VAR1 -eq 2]
then
    echo "Var 1 is 2"
fi
# check if file has errors
#!/bin/bash -n
# number of arguments passed
$#
# path of file
$0
# filename only
'basename $0'
# for loop
for i in "$@"
do
    echo $i
done
# define variable
VAR1 = "hello"
# use variable
my_function $VAR1
my_function ${VAR1}

# while loop
count=0
while [ $count -lt 5 ]
do
    echo "hello"
    sleep 1
    count=$((count+1))
done
# infinite loop
while [ 1 ]
while :
while true
# one liner
while :;do pwd; sleep 1; done

# until loop (do until condition gets true)
count=3
until [ $count -le 0 ]
do
    echo "hello"
    count=$((count+1))
    sleep 1
done
# infinite until loop
until false
until [ 0 ]

# for loop
for VAR in 1 2 3 a b c
do
    echo $VAR
done
# for in range increment 1
for i in {1..25}
# for in range increment by 2
for i in {1..50..2}
for i in $(seq 0 2 50)
for (( c=1; c<=5; c++))
for i in `seq 2 50`
for i in ${my_array[@]}
# infinite for in range loop
for (( ; ; ))

# if condition
if [ $VAR -lt 5 ]
then
    echo "hello"
elif [ $VAR -lt 2 ]
    echo "hi"
then
else
    echo "good bye"
fi
# or
if [ condition1 ] || [ condition2 ]
# and
if [ condition1 ] && [ condition2 ]
# compare numbers: -lt -gt -get -let -eq -ne
$VAR -lt 5
# compare strings with = or !=
$VAR = 'test'

# string interpolation
printf "Test variable is \n $VAR \n"

# file expressions
# check if file/directory exists
filename="test.txt"
if [ -e $filename ]
# check if its a regular file
if [ -f $filename ]
# check if block device file (usb device) -> reads in blocks, not in characters
if [ -b $filename ]
# check if characer device file (mouse, keyboard) -> 1 character at a time
if [ -c $filename ]
# check if its directory
if [ -d $filename ]
# check if length of string is not zero
if [ -n "$VAR" ]
# check if length of string is zero
if [ -z "$VAR" ]
# see test expressions
man test


## get user input
# read input into variable
read VAR
# read only two characters
read -n2 VAR
# read into an array
read -a MY_ARR

# Case Switch
case $VAR in
    1) echo "VAR is one"
        ;;
    2) echo "VAR is two"
        ;;
    *) echo "VAR is not one or two"
        ;;
esac


## File handling
# read line by line of file but opens a new shell with pipe
cat test.txt | whiel read LINE
do
    echo $LINE
done
# same, but without opening a new shell
while read LINE
do
    echo $LINE
done < test.txt


## Exit status
# previous exit status
echo $?
# 0 is ok; != 0 is error in range 0 - 255


## Random number
# generate random number
echo $RANDOM
# generate random number between 1 and 10
echo $RANDOM%10


## Arrays
# declare array
declare -a my_array
my_array[0] = "hello"
my_array[1] = "world"
# or declare like
my_array=(1 2 "test 1" "test 2")
# or declare like
my_array=([0]=1 [2]="test 1" 4)
# or read from input
read -a my_array
# access
echo ${my_array[0]}
# get length of array with #
echo ${#my_array[@]}


## Here document
# multiline comments
<< MYCOMM
    this is a comment
    this is also a comment
MYCOMM
# add inputs non-interactive
ftp -n $ftp_server << EOF
quote USER $user_name
quote PASS $password
EOF


## Trap and signals
# signals = for ipc (inter process communication)
# list all signals
kill -l
# CTRL + C is signal 2) SIGINT = signal interruption
# trap: catches a signal
trap 'echo "process killed"' SIGINT
# see process id if file test.txt
ps -ef | grep test
# send signal 1 to process
kill -1 pid
# trap and kill
trap 'echo "process killed"; exit 1' SIGINT SIGTRAP SIGHUP
# use function and pass sig id to function
trap 'my_func SIGINT; exit 1' SIGINT
trap 'my_func SIGHUP; exit 1' SIGHUP
#  remove trap
trap - SIGINT


## dd df, du, Isof, netstat
# generate a test file
dd if=/dev/zero of=test.txt bs=1024 count=100
# copy a file
dd if=test.txt of=test1.txt bs=1024
# show disk free space
df
# human readable
df -kh
# du = disk usage: show disk usage of folders
du
# list open files
lsof
# netstat - network info
netstat -nap
# list hardware statistics
lscpu
lsusb
lspci
# system information
dmidecode


## attach/mount disk
# attached disks must be partitioned, formatted and mounted
# partition
fdisk /dev/sdb # add new partition
# format
mkfs.ext4 /dev/sdb1
# mount
mount -t ext4 /dev/sdb1 /mnt/mydisk


## nmap network and port info
# scan for open ports
nmap -T4 -A -v 192.168.240.1


## ssh, scp, sshpass
# ssh to remote machine (-Y for gvim)
ssh -p 22 root@192.168.2.1 -Y
# copy file to current directory
scp -P22 root@192.168.2.1:/home/user/test.txt .
# use sshpass
sshpass -p my_password -p22 -oStrictHostKeyChecking=no root@192.168.2.1


## tcpdump
# take a network dump
tcpdump -i eth0 -n dst '192.168.2.1'
