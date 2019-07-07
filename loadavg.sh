#!/bin/ksh 

PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin

set -a 

if [[ $(id -u) != 0 ]]
then
	print "\033[31mCRITICAL: Please make sure you have root privilege...\033[00m"
        exit 1
fi
server=`hostname`
OS=`uname -s`
host=$(hostname -s|cut -d- -f2|sed s/[0-9]//g)
print "Checking load on $OS host $server"
Num_CPU=`system_profiler|egrep -i 'of processor'|cut -d: -f2|sed 's/ //g'`
CPUCORE=`system_profiler|egrep -i 'cores'|cut -d: -f2|sed 's/ //g'`
#print "\n$Num_CPU"
print "Number of cpu cores:$CPUCORE"

CRITICAL=$(print $CPUCORE*1|bc)
WARNING=$(print $CRITICAL*0.85|bc)
IDLE=0

#Check_load

LOAD_AVG=`uptime|awk '{ print "1min\t5mins\t15mins\n"$10"\t",$11,"\t",$12 }'`
LOAD1=`uptime |awk '{print $10}'`
LOAD5=`uptime |awk '{print $11}'`
LOAD15=`uptime |awk '{print $12}'`

print "Current load avg is:\n$LOAD_AVG"

if [[ "$LOAD1" -eq "0" ]]
	then
	print "\033[33mThe CPU is IDLE\033[00m"
elif [[ "$LOAD5" -lt "$WARNING" && "$LOAD15" -lt "$WARNING" ]]
	then
	print "\033[36mOK:The load avg is $LOAD1,$LOAD5,$LOAD15\033[00m"	

elif [[ "$LOAD5" -ge "$CRITICAL" && "$LOAD15" -ge "$CRITICAL" ]]
	then
	print "\033[31mThe load is critical\033[00m"
	print "The syslogd needs restart"
	print "\033[36m Restarting syslogd\033[00m"
fi

#Check_system_log

Log_lines=`wc -l /var/log/system.log|sed 's/\/var\/log\/system\.log//'|sed 's/ //g'`
print "No of loglines:$Log_lines"

#cat /var/log/system.log|grep -i 'logfile turned over'

#Restart_syslogd

#sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.syslogd.plist


#Cross_check_whether_its_stopped


SYSLOGD=`ps -ef|grep syslogd|wc -l`

if [[ $SYSLOGD -ge "2" ]]
	then
	print "The syslogd instance is running"
#	sudo killall syslogd
else
	print "The syslogd instance is stopped"
fi
