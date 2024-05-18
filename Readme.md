
# 项目介绍
    基于BBCOS的系统,未来希望可以变成主流系统
 
    
 
# 环境依赖
 见git/pip.txt
 openai
 PyQt5
 PyQt5-tools
 
# 目录结构描述
PythonOS  //根目录

    ├── Readme.md           // 帮助文档

    ├── start.sh   //启动程序

    ├──bootloader.py    //kernel.py的引导程序,可以选择GUI版本和纯命令行版本

    ├── Oos.ico    //启动动画

    ├── command.txt    //命令行支持

    └──PythonOSsys   //系统文件夹

       ├── kernel.py    // 系统主体 python脚本文件

       ├── GUI.py             // GUI,未来的桌面

       ├──debugOS.py //为了优化bootloader启动程序而保存的1.2版本精简PythonOS

    └──git   //github所需要的说明

       ├──bugs.txt    //漏洞的提交和查看

       ├──pip.txt      //需要的依赖

       ├──README.md.bak    //旧版readme.md帮助文档

    └──devfile    //开发区,开发所用

       ├──bt.py     //用于测试

       ├──bt(ofpyos).py    //用于测试,专门为pythonos优化的版本!

       ├──GUI.ui    //桌面体验的设计文件

       ├──newui.UI   //更新的ui

    └──apps     //apps文件

       └──app文件可以自由下载和安装所以不写
 
# 使用说明
       单独下载的需要     <pip install pip.txt>
       之后    <sh start.sh>
 
# 版本内容更新
###### v1.1.24.05.05.DEV: 
      实现跨文件夹交互
      实现基于Linux的单独启动(ubuntu) 

###### v1.1.24.05.11.DEV: 
      紧急修复跨文件夹的python报错
      新增ls显示真实目录
      新增多文件夹

###### v1.1.24.05.18.DEV: 
      紧急修复跨文件夹的python报错
      更新privim
      更新了BBCOS©️的版本(1.2👉1.4)
      

# user
#####user:root
#####passwd: adminpasswd
