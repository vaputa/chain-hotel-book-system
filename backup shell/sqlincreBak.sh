#! /bin/bash
#定义一个标识脚本正在执行的文件名，尽量让这个临时文件名独特
#避免与他处指定重名，可借鉴C/C++防止重复包含头文件的宏命名法
TMPFILE=/tmp/sqlincreBak.sh.tmp
 
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
#     guo     first
# Path
#    ....
BakBaseDir=/root/mysql/backup
[ ! -e "$BakBaseDir" ] && mkdir -p $BakBaseDir
BakDir=$BakBaseDir/daily
[ ! -e "$BakDir" ] && mkdir -p $BakDir
LogFile=$BakBaseDir/bak.log

BinDir=/var/log/mysql
#[ ! -e "$BinDir" ] && mkdir -p $BinDir
BinFile=$BinDir/mysql-bin.index

mysqladmin -uhotel -photel flush-logs
#这个是用于产生新的mysql-bin.00000*文件
Counter=`wc -l $BinFile |awk '{print $1}'`
NOW=`date -d "today" +"%Y%m%d_%H%M%S"`
DumpFile=$NOW'_inc'.sql
GZDumpFile=$NOW'_inc'.sql.tgz
NextNum=0
#这个for循环用于比对$Counter,$NextNum这两个值来确定文件是不是存在或最新的。
for file in  `cat $BinFile`
do
        base=`basename $file`
        #basename用于截取mysql-bin.00000*文件名，去掉./mysql-bin.000005前面的./
        NextNum=`expr $NextNum + 1`
        if [ $NextNum -eq $Counter ]
        then
                echo $base skip!  >> $LogFile
        else
                dest=$BakDir/$base
                if(test -e $dest)
                #test -e用于检测目标文件是否存在，存在就写exist!到$LogFile去。
                then
                        echo  $base exist! >> $LogFile
                else
                        cp $BinDir/$base $BakDir
                        mysqlbinlog $BakDir/$base >> $DumpFile
                        tar czvf $GZDumpFile $DumpFile
                        scp -r $GZDumpFile lab@10.131.255.124:~/bak/database/
                        rm $DumpFile
                        rm $GZDumpFile
                        echo $base copying >> $LogFile
                fi
        fi
done
echo `date +"%Y年%m月%d日 %H:%M:%S"` $Next Bakup succ! >> $LogFile