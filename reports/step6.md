# Step6实验报告 

#### 计81 卢星宇 2018011280

## 任务概述

1. 改进语法
2. IR标识符加入Label，Branch
3. 实现LabelManager来管理Label，为做区别，采用和参考实现同样的办法：在相同的label后面加上编号
4. Asm实现Label和Branch的编译。



## 遇到的困难

在利用list向Asm传输不同IR标识符时，出现了顺序相反的问题，所以改为一次只传输一个标识符。

在实现br指令时遇到了问题，查看参考实现之后明白了将t1, t2都置为0的巧妙方法。

## 思考题

### 第一题

答：将分支用大括号包裹起来可以避免else找不到对应的if，即解决了悬吊else问题，if和else能够更好地一一对应。

## 代码参考

参考了参考实现step6的labelManager和branch实现方法。

