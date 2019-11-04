data_section = {"db": 1, "dw": 2, "dd": 4, "dq": 8}
bss_section = {"resb": 1,"resw": 2,"resd": 4,"resbq": 8 }
opcode = ["mov", "add", "inc", "jmp", "cmp", "push", "sub", "mul", "or", "xor", "dec", "call"]
reg = {"eax": "000", "ecx": "001", "edx": "010", "ebx": "011", "esp": "100", "ebp": "101", "esi": "110", "edi": "111"}

ERROR = list()


def check_Data_Section(str1):
    k = 0
    for i in data_section.keys():
        if str1 == i:
            return 1
    return 0

def Check_data_size(str):
    for i,j in data_section.items():
        if i == str:
            return j
    return 0

def Check_Bss_Section(str1):
    k = 0
    for i in bss_section.keys():
        if i == str1:
            return 1
    return 0

def Check_bss_size(str):
    for i, j in bss_section.items():
        if i == str:
            return j
    return 0

def Repate_variable(line, str, lst):
    for i in range(len(lst)):
        if lst[i][2] == str:
            if str != "main":
                ERROR.append("File.asm:{}: error: symbol `{}' redefined".format(line, str))
                return 0
    return 1

def Return_Addr_id(lst1):
    str1 = ""
    for i in range(len(lst1)):
        line = (hex(ord(lst1[i])))
        str = (line.split("x"))
        str1 += str[1]
    return(id(str1))

def Check_Opcode(str1):
    for i in opcode:
        if str1 == i:
            return 1;
    return 0

def Check_Reg(str1):
    for i in reg.keys():
        if str1 == i:
            return 0;
    return 1

def Check_variable(str, lst):
    for i in range(len(lst)):
        if lst[i][2] == str:
            lst[i][4] = "D"
    return 1