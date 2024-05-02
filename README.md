# MOLinux
基于BBCOS的系统,未来希望可以变成主流系统

# 启动条件
在Unix和类unix(Linux,macOS)设备中运行,或者已经安装了git的Windows和任何可以执行.sh文件的设备上运行(不管你是神仙还是人,你都得安装python3)
                                    pip3 instal pip.txt
                                     bash start.sh

# 贡献
银狐furry
https://blog.csdn.net/qq_62293794/article/details/128476017
提供内核代码
# 后记
账号:sysroot
密码:adminpasswd
别点sneix.py,这是直接下载下来的,不确定可不可以运行,还没修改,不知道干什么的(好像是python小游戏,从老师那里连移植都没移植的东西)
# 特别告示栏
在1.24.05.02中,移除了MLX,新增了用户机制,新增了对桌面的支持,预计在下一个版本中添加桌面,bombom是射击小游戏,但因未知原因,没有敌人
⚠️注意!老用户请重新安装一遍pip.txt
⚠️注意!在该版本中,我们的正式版已经停更,请不要害怕,之前的正式版下载链接还在
一共530行代码
请先安装pip.txt里面的东西再运行,新增app(输入vim开启)
# 可以UEFI启动
如果您想让它在逻辑上运行的话,那么请创建一个vertoy启动盘,之后在虚拟机中创建一个(符合您的soc或cpu指令集的,比如arm64,amd64)ubuntu系统(最好启动一个自带python3的Linux内核,ubuntu只是它的之后的封装原理),最好是只有命令行的,之后,在上面安装python,安装好pip和pip模块,再git下来本项目,将该项目放到patch,名字叫pyos,位置在
"/home/pyos(或者你的用户名)/本项目名称/start.sh"
之后在终端执行systemctl start pyos,再将虚拟机断电,再将虚拟机磁盘文件移到vertoy磁盘里面,就可以享受啦!
当然,在之后本项目提供的镜像,是开箱即用的,不用再配置,以上内容只能代表其工作原理,不一定是成品
# 可以运行的程序
之后专门设计的安装器会释放py文件,之后修改app_api.py,但你也可以强制让pyos被杀死,之后运行别的py和Linux软件,或者你可以下载一个py程序,之后在app_api.py中手动写入即可运行
# 程序兼容性:
 pythonOS直接运行被基于pythonOS的py程序=100%支持!(完美运行)
 pythonOS运行普通py文件=在结束时可能不会返回pythonOS,进而导致接触到Linux内核,这是一个漏洞!=60%(基本只支持吧...)
 pythonOS运行别的啥玩意=不知道这是啥,运行不了

 # 漏洞整合
 漏洞危险等级:ZAYIN(安全),TETH(普通危险),HE(严重危险),WAW(及其危险!),ALEPH(毁灭性的,非常规的严重,最危险!)
 漏洞格式: PYS-年月日-字第几行或出处-关系到的东西
 字:R:readme.md的#K:kernel的很少见,很严重#N:别的啥玩意吧  关系到的东西:SYSCORE,kernel.py的或是可以直接获取到Linux运行kernel.py的内核系统的严重危害漏洞,全是ALEPH级别的
 PYS-240502-R32-SYSCORE:出处:readme第32行,严重等级:ALEPH-非常严重-未证实-容易接触到系统底层,很危险


