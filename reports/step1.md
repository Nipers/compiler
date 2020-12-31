# Report  of Step1

**计81 卢星宇 2018011280**

## 任务概述

1.编写语法分析TokenKind列表和词法分析rules字符串

2.学习使用ANTLR工具生成lexer和parser

3.从AST生成IR

4.从IR生成ASM汇编代码，IR指令为Ret和Const

## 遇到的困难：

参考实现的代码结构较为复杂，读了很长时间才将各部分功能对应完毕。

参考实现最初版本和最终版本之间结构存在差异，根据最初版本复现出的代码无法通过测试，调了很久都没成功，根据室友的指示才完成调试

## 代码结构

#### 主函数main.py

工作流程如下：

1.获取输入文件名并读入文件

2.利用lexer处理输入文件生成tokenStream

3.利用parser处理tokenStream生成语法分析树tree

4.利用GenerateIR函数调用StackIRGen函数处理tree生成中间码IR

5.利用GenerateASM函数处理IR生成汇编代码

#### IRGen

StackIRGen是逻辑部分，采用visitor模式，对语法分析树进行解析，这里只有Integer和Ret两种节点

IREmitter负责对IR栈进行操作，目前只需要处理func，并判断函数名称是否为main

#### AsmGen

采用visitor设计模式，依次翻译各个函数产生的IR指令为汇编代码，负责栈帧的分配和回收。



## 思考题

#### 第一题

修改 minilexer 的输入（lexer.setInput 的参数），使得 lex 报错，给出一个简短的例子。

#### 答案：

可以在输入文件任意位置添加一个中文字符，如：

```C++
int main() {
     return 233;
     我
}        
```

报错如下：

```输出结果
token kind   text                

-----------  -------------------

Int          int                 
Ident		 main                
Lparen       (                   
Rparen       )                   
Lbrace       {                   
Return       return              
Integer      233                 
Semicolon    ;                   
Traceback (most recent call last):
  File "minilexer.py", line 95, in <module>
    dumpLexerTokens(default())
  File "minilexer.py", line 90, in dumpLexerTokens
    for tok in lexer.lex():
  File "minilexer.py", line 45, in lex
    raise Exception(f"lex error at input position {self.pos}")
Exception: lex error at input position 45
```

#### 第二题

修改 minilexer 的输入，使得 lex 不报错但 parse 报错，给出一个简短的例子。

#### 答案：

例子：

```c++
int int main() {    
  return 233;
}  
```

lexer输出：

```lexer
token kind   text                

-----------  -------------------

Int          int                 
Int          int                 
Ident	     main                
Lparen       (                   
Rparen       )                   
Lbrace       {                   
Return       return              
Integer      233                 
Semicolon    ;                   
Rbrace       }  
```

parser报错：

```parser
Traceback (most recent call last):
  File "miniparser.py", line 71, in <module>
    print(default().parse("program"))
  File "miniparser.py", line 45, in parse
    children.append(self.parse(child))
  File "miniparser.py", line 42, in parse
    raise Exception(f"syntax error, {child} expected but {tok.kind.name} found")
Exception: syntax error, Ident expected but Int found
```

#### 第三题

在 riscv 中，哪个寄存器是用来存储函数返回值的？

#### 答案

是寄存器a0

## 代码参考情况：

照搬了参考实现的Makefile和祖传CommonLex.g4

采用参考实现的框架实现step1，包括visitor模式，IRGen，ASMGen的部分内容

