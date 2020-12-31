class AsmCommand:
    def __init__(self, s):
        self.s = s
    def __repr__(self):
        return self.__str__()
#一条命令写入的形式有多种，指令，标签，注释，空白都有可能
class AsmInstructor(AsmCommand):
    def __str__(self):
        return f"\t{self.s}"

class AsmLabel(AsmCommand):
    def __str__(self):
        return f"{self.s}:"

class AsmDirective(AsmCommand):
    def __str__(self):
        return f"\t{self.s}"

class AsmComment(AsmCommand):
    def __str__(self):
        return f"\t#{self.s}"

class AsmBlank(AsmCommand):
    def __init__(self):
        pass
    def __str__(self):
        return f""