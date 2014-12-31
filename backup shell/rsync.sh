#!/bin/bash
#定义一个标识脚本正在执行的文件名，尽量让这个临时文件名独特
#避免与他处指定重名，可借鉴C/C++防止重复包含头文件的宏命名法
TMPFILE=/tmp/rsync1.sh.tmp
 
# BEGIN--检查是否有别的实例在运行，保证同时只能运行一个实例
 
if [ -e $TMPFILE ]  #判断临时文件是否存在
then                
   echo "Other instance is running!" #存在表明有一个实例在运行
   exit 0           #退出本脚本的执行
else
   touch $TMPFILE   #监时文件若不存在,就用 touch 新建一个
   chmod 600 $TMPFILE #把临时文件属性改为只建立者可读写
fi
 
#用 trap 命令设置一个对信号的监听器
#程序运行中当监听到信号 0,1,2,3,9,15就会删除临时文件，并退出脚本执行
#比如说，当脚本自行运行结束、被用户 Ctrl+C 掉、被 Kill 掉、终端被关闭
#系统关机或重启的情况下，都需将临时文件删除，否则脚本以后都没机会执行
#在 Linux 的 shell 下可以运行 trap -l 查看到所以信号
trap "rm -f ${TMPFILE}; exit" 0 1 2 3 9 15
 
# END--检查是否有别的实例在运行，保证同时只能运行一个实例
 
#下面是这支 Shell 要完成的任务的代码了
unset verb progress
for i in $*; do
[ "$i" = "verb" ] && verb=v
[ "$i" = "progress" ] && progress="--progress"
done

RSYNC_SERVER=10.131.244.124 #rsync server IP
backupDir=/home/lab/chain-hotel-book-system


databaseDir=$backupDir/database
[ ! -e "$databaseDir" ] && mkdir -p $databaseDir
AUTH_USER=backup
weekid=$(($(($(date +%s) - $(date +%s -d '2014-08-03 00:00:00')))/(3600*24*7)))
BAKROOT=$backupDir/Week$weekid
INC_DIR=increment
NOW=`date +%Y-%m-%d_%H:%M`


WEEKDAY=`date +%w`  #判断是一周中的周几,如果是周日0进行完全备份


logRoot=/var/log/rsync
[ ! -e "$EXCLUDES" ] && mkdir -p $BAKROOT
[ ! -e "$EXCLUDES" ] && mkdir -p $logRoot

PASSWD_FILE=/etc/rsyncpass.conf
PASSWD_PERM=`ls -l $PASSWD_FILE|awk '{print $1}'`
if [ "$PASSWD_PERM" != "-rw-------" ]; then
echo -e "\nWARNING: permission of passwd file changed to 0600 \n";
chmod 0600 $PASSWD_FILE
fi

LOGFILE=/var/log/rsync/rsyncbak.log
EXCLUDES=/var/log/rsync/exclude_file
[ ! -e "$EXCLUDES" ] && touch $EXCLUDES

BACKUP_MODULES="testdata" #如需备份多个目录，在“”内添加server端的模块名，用空格隔开

rm -f /var/log/rsync/log.*
log_id=0
for bakdir in $BACKUP_MODULES; do
log_id=`expr $log_id + 1`
#SUBOPTS="$BAKROOT/$INC_DIR/$bakdir/$NOW -az${verb}"
#SUBOPTS="$BAKROOT/$INC_DIR/$bakdir/$NOW"
SUBOPTS="$BAKROOT/$INC_DIR/$NOW"
SOURCE="$AUTH_USER@$RSYNC_SERVER::$bakdir"

if [ $WEEKDAY -eq 0 ];then
rsync -aHxv  --password-file=$PASSWD_FILE $SOURCE $BAKROOT/$bakdir/ | tee /var/log/rsync/log.$log_id
else
[ ! -e "$SUBOPTS" ] && mkdir -p $SUBOPTS
rsync -axv  --password-file=$PASSWD_FILE --compare-dest=$BAKROOT/$bakdir/ $SOURCE $SUBOPTS | tee /var/log/rsync/log.$log_id
cat /var/log/rsync/log.* >>$SUBOPTS/increbak.log
fi
done

### 合并临时日志到备份日志中
cat /var/log/rsync/log.* >> $LOGFILE
rm -f /var/log/rsync/log.*
##### end of rsync.sh file trans


