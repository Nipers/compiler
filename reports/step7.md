# 实验报告

#### 计81 卢星宇 2018011280

## 任务概述

1. 改进语法，新增对块语句的支持
2. 使用名称解析，新建NameManager类以管理变量名称，其中有一个variables字典列表和decal字典列表，分别用以存储当前作用域中的变量和开作用域中的变量，进入作用域则新建一个字典并压栈，出作用域则将作用域字典弹出。



## 遇到的困难

块语句支持之前已经实现，这一步只是将之前的名称解析部分拆成独立的模块并略微改动main函数内容，所以没有遇到较大的困难。



## 思考题

### 第一题

```c
int main() {
 	int x = 0;
 	if (x) {
     	return x;
 	}
    else {
     	int x = 2;
 	}
 	return x;
}
```

### 第二题

答：例如java，Python这些语言的类函数可以在声明之前被调用，编译器在读取函数调用之前无法得知函数信息，这种语言的名称解析作为单独的一个阶段在 IR 生成之前执行会更好