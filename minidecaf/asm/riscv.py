from .command import AsmInstructor
from ..ir.instructor import *
from ..ir import *
from ..utils import INT_BYTES
from ..utils import flatten
from .command import *

#将指令转化为对应的汇编代码

def Instructors(f):
    def g(*args, **kwargs):
        instructors = f(*args, *kwargs)
        return [(AsmInstructor(x) if type(x) is not AsmInstructor else x) for x in instructors]
    return g

@Instructors
def push(val):
    if type(val) is int:
        return [f"addi sp, sp, -{INT_BYTES}", f"li t1, {val}", f"sw t1, 0(sp)#push"] #push an integer into stack
    else:
        return [f"addi sp, sp, -{INT_BYTES}", f"sw {val}, 0(sp)#push"] #push a register into stack

def Push(*vals):
    return flatten(map(push, vals))

@Instructors
def pop(reg):
    return ([f"lw {reg}, 0(sp)"] if reg is not None else []) + [f"addi sp, sp, {INT_BYTES}#pop"]


def Pope(*regs):
    return flatten(map(pop, regs))

@Instructors
def unary(op):
    op = {'-': "neg", '!': "seqz", '~': "not"}[op]
    return pop("t1") + [f"{op} t1, t1"] + push("t1")

@Instructors
def binary(op):
    b1 = { "+": "add", "-": "sub", "*": "mul", "/": "div", "%": "rem" }
    b2 = { "==": "seqz", "!=": "snez" }
    b3 = { "<": "slt", ">": "sgt" }
    if op in b1:
        return Pope("t2", "t1") + [f"{b1[op]} t1, t1, t2"] + push("t1")
    if op in b2:
        return Pope("t2", "t1") + [f"sub t1, t1, t2", f"{b2[op]} t1, t1"] + push("t1")
    if op in b3:
        return Pope("t2", "t1") + [f"{b3[op]} t1, t1, t2"] + push("t1")
    if op == "||":
        return Pope("t2", "t1") + [f"or t1, t1, t2", f"snez t1, t1"] + push("t1")
    if op == "&&":
        return pop("t2") + unary("!") + push("t2") + unary("!") + binary("||") + unary("!")
    if op == "<=":
        return binary(">") + unary("!")
    if op == ">=":
        return binary("<") + unary("!")

@Instructors
def load():
    return pop("t1") + ["lw t1, 0(t1)"] + push("t1")#取地址，根据地址取数，存数

@Instructors
def store():
    return Pope("t2", "t1") + ["sw t1, 0(t2)"] + push("t1")#取地址，取数，存数，将数压回

@Instructors
def frameSlot(offset):
    return Push("fp", offset) + binary("+")#这里明白了是将栈帧和offset存入栈中然后通过binary取出，求和并存回栈中

@Instructors
def ret(function:str):
    return [f"beqz x0, {function}_exit#RET"]

@Instructors
def branch(op, label):
    if (op == "br"):
        return Push(*[0, 0]) + branch("beq", label)
    elif (op == "beqz"):
        return push(0) + branch("beq", label)
    elif (op == "bnez"):
        return push(0) + branch("bne", label)
    else:
        return Pope("t2", "t1") + [f"{op} t1, t2, {label}" ]

@Instructors
def label(label:str):
    return [f"{label}:"]

@Instructors
def call(funcName:str, paramNum:int):
    return [f"call {funcName}"] + Pope(*[None] * paramNum) + push("a0")

@Instructors
def globalSymbol(symbol:str):
    return [f"la t1, {symbol}"] + push("t1")

class AsmGenerator:#用于集中生成汇编代码
    def __init__(self, emitter):
        self.emitter = emitter
        self.curFunc = None
        self.curParamInfo = None

    def generateRet(self, instr:Ret):
        self.emitter(ret(self.curFunc))

    def generateConst(self, instr:Const):
        self.emitter(push(instr.value))
    
    def generateUnary(self, instr:Unary):
        self.emitter(unary(instr.op))

    def generateBinary(self, instr:Binary):
        self.emitter(binary(instr.op))
    
    def generateFrameSlot(self, instr:FrameSlot):
        self.emitter(frameSlot(instr.offset))
    
    def generateLoad(self, instr:Load):
        self.emitter(load())
    
    def generateStore(self, instr:Store):
        self.emitter(store())

    def generatePop(self, instr:Pop):
        self.emitter(Pope(None))

    def generateBranch(self, instr:Branch):
        self.emitter(branch(instr.op, instr.label))

    def generateLabel(self, instr:Label):
        self.emitter(label(instr.label))

    def generatePrologue(self, function:IRFunc):#根据函数生成指令段
        self.emitter(
            [
            AsmBlank(),
            AsmDirective(".text"),
            AsmDirective(f".globl {function.name}"),
            AsmLabel(f"{function.name}")
            ]
            + Push("ra", "fp") +
            [
            AsmInstructor("mv fp, sp"),
            AsmComment("copy args:")
            ])
        for i in range(function.paramNum):
            frm = INT_BYTES * (i + 2)
            self.emitter([f"lw t1, {frm}(fp)"] +
            push("t1"))  
        self.emitter([
            AsmComment("END PROLOGUE"),
            AsmBlank()])

    def generateEpilogue(self, function:IRFunc):
        self.emitter([
            AsmBlank(),
            AsmComment("BEGIN EPILOGUE")]
            +push(0)+
            [AsmLabel(f"{function.name}_exit"),
            AsmInstructor("lw a0, 0(sp)"),
            AsmInstructor("mv sp, fp")]
            + Pope("fp", "ra") +
            [AsmInstructor("jr ra"),
            AsmBlank()]
        )

    def generateCall(self, instr:FuncCall):
        nothing, func = listFind(lambda func: func.name == instr.funcName, self.ir.funcs)
        self.emitter(call(func.name, func.paramNum))

    def generateGlobalSymbol(self, instr:GlobalSymbol):
        self.emitter(globalSymbol(instr.symbol))

    def generateFunc(self, func:IRFunc):
        self.curFunc = func.name
        self.generatePrologue(func)
        for instructor in func.instrs:
            self.emitter([
                AsmComment(instructor)
            ])
            process[type(instructor)](self, instructor)
        self.generateEpilogue(func)

    def generateGlobal(self, glob:IRGlobal):
        if glob.init is None:
            self.emitter([AsmDirective(f".comm {glob.sym},{glob.size},{glob.align}")])
        else:
            self.emitter([
                AsmDirective(".data"),
                AsmDirective(f".globl {glob.sym}"),
                AsmDirective(f".align {glob.align}"),
                AsmDirective(f".size {glob.sym}, {glob.size}"),
                AsmLabel(f"{glob.sym}"),
                AsmDirective(f".quad {glob.init}")
            ])    

    def generate(self, ir):
        self.ir = ir
        for glob in ir.globs:
            self.generateGlobal(glob)
        for function in ir.funcs:
            self.generateFunc(function)
process={Ret: AsmGenerator.generateRet, Const: AsmGenerator.generateConst,
        Unary: AsmGenerator.generateUnary, Binary: AsmGenerator.generateBinary,
        Comment: nothing, FrameSlot: AsmGenerator.generateFrameSlot,
        Load: AsmGenerator.generateLoad, Store: AsmGenerator.generateStore,
        Pop: AsmGenerator.generatePop, Branch: AsmGenerator.generateBranch,
        Label: AsmGenerator.generateLabel, FuncCall:AsmGenerator.generateCall,
        GlobalSymbol: AsmGenerator.generateGlobalSymbol
        }#用于将不同指令映射到对应的转换函数