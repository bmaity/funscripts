#!/bin/bash
expect=/usr/bin/expect
ssh=/usr/bin/ssh
PATH=/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/y/bin64:/home/y/bin:/usr/lib64/qt-3.3/bin
expectcmd=/tmp/expect.cmd.$$

if [ $# -lt 1 ]
then
echo -e "Usage: $0 [-h hostname] | [-f tgt-file] -c command\n"
exit 0
fi


while getopts 'c:f:|h:' OPT_LETTER
do

case "$OPT_LETTER" in
    c) command="$OPTARG" ;;
    f) target="$OPTARG"
	if [ -f $OPTARG ]
	then
		hosts=`cat $OPTARG`
	else
		echo -e "File does not exits...\n"
		exit 0;
	fi
;;
    h) hosts="$OPTARG" ;;
    *) echo -e "Usage: $0 [-h hostname] | [-f tgt-file] -c command\n"; exit 0 ;;
    esac
done

echo -e "command(s) to run on Host(s) : $hosts\n"
echo -e "Command is : $command\n"
echo -e "Tgt-File is :$target\n"
echo -n "Please enter your password: "
stty -echo
read password 
stty echo

for onehost in $hosts
do
  echo -e "\n==========================================\n";
  echo " ---------- $onehost -------";

cat > $expectcmd << EOF_expect;
#!/usr/bin/expect -f 
set timeout -1
stty -echo
spawn ssh -t -q -o StrictHostKeyChecking=no $onehost -A "$command"
expect eof {exit 2} Bad {exit 2} timeout {exit 1} "assword:" { send "$password\n" }
stty -echo
expect eof {exit 2} Bad {exit 2} timeout {exit 1} "$USER:" {stty -echo; send "$password\n" }
expect eof {exit 0} Bad {exit 2} timeout {exit 1}
EOF_expect

  chmod 755 $expectcmd
  $expectcmd|grep -v spawn|grep -v password

done
rm -f /tmp/expect.cmd.*
stty echo
