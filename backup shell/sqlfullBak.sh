#! /bin/bash
#定义一个标识脚本正在执行的文件名，尽量让这个临时文件名独特
#避免与他处指定重名，可借鉴C/C++防止重复包含头文件的宏命名法
TMPFILE=/tmp/sqlfullBak.sh.tmp
 
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

# Program
#    use mysqldump to Fully backup mysql data per week!
# History
#    2013-04-27 guo     first
# Path
#    ....
BakDir=/root/mysql/backup
[ ! -e "$BakDir" ] && mkdir -p $BakDir
BakDirDaily=$BakDir/daily
[ ! -e "$BakDirDaily" ] && mkdir -p $BakDirDaily
LogFile=$BakDir/bak.log
Date=`date +%Y%m%d`
Begin=`date +"%Y%m%d %H:%M:%S"`
cd $BakDir
DumpFile=$Date'_full'.sql
GZDumpFile=$Date'_full'.sql.tgz
mysqldump -uguo -pguo1234 --quick --all-databases --flush-logs --delete-master-logs --single-transaction > $DumpFile
#mysqldump -uguo -pguo1234 --quick everlive --flush-logs --delete-master-logs --single-transaction > $DumpFile  #对于单个everlive数据库日志
tar czvf $GZDumpFile $DumpFile
scp -r $GZDumpFile root@test.everlive.me:~/bak/database/
rm $DumpFile
Last=`date +"%Y%m%d %H:%M:%S"`
echo Begin:$Begin End at:$Last $GZDumpFile succ >> $LogFile
cd $BakDir/daily
rm -f *