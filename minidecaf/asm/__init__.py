from .command import *
from .riscv import AsmGenerator as Gen
#asm文件夹的作用是将原本的IR指令转化为汇编代码

def asmGen(ir, fout):
    asmEmitter = AsmEmitter(fout)
    Gen(asmEmitter).generate(ir)

class AsmEmitter:
    def __init__(self, fout):
        self.fout = fout

#emit函数，把命令写入文件
    def emit(self, command:AsmCommand):
        print(f"{command}", file = self.fout)
    
#集中写入
    def __call__(self, commands:[AsmCommand]):
        for command in commands:
            self.emit(command) 