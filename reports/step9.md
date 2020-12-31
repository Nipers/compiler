# 实验报告

#### 计81 卢星宇 2018011280

## 任务概述 

1. 改进语法，添加函数声明，函数定义，函数调用等语句
2. 改进NameManager，增加FuncInfo类对声明的function进行管理

## 遇到的困难

这一步一开始很顺利，甚至跑完step10的testcase都没有碰到问题，直到开始测试failcase时，发现有些检测，例如对函数参数和内部变量同名的检测没有实现，我很奇怪为什么参考代码里也没有实现，后来得知参考代码的step9没有实现这一点，所以用我自己的方法实现了。

## 思考题

考虑如下两个程序：

#### 程序1

`int sum(int a, int b) {`

`		return a + b;`

`}`

`int main() {`

​	`int a = b = 0;`

`		return sum(a = b + 1, b = 1 + 2);`

`}`

#### 程序2

`int sum(int a, int b) {`

`		return a + b;`

`}`

`int main() {`

​	`int a = b = 0;`

`		return sum(b = 1 + 2, a = b + 1);`

`}`



依照我写的编译器，第一个程序的返回值为7,第二个程序的返回值为4,由此可见，如果参数的表达式进行了赋值操作，我的实现是从右向左依次计算参数的值，所以交换两个表达式会使结果不同，但完全可以从左向右进行计算，所以是未定义行为。
