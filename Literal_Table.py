import Object_pyc as OP
import re

Literal = list()

def Literal_Table_File():
    f = open("File.asm", "r")
    line = f.readlines()
    no = 0
    cnt = 0
    for i in line:
        no += 1
        str1 = (re.split(r'[.:,\s]\s*', i))

        lit = list()
        if OP.Check_Opcode(str1[1]):
            if str1[3] != "":
                if OP.Check_Reg(str1[3]):
                    cnt += 1
                    lit.append(no)
                    lit.append(cnt)
                    lit.append(str1[3])
                    Literal.append(lit)

    if len(OP.ERROR) != 0:
        return
    print("\n\n\n\t\t\t\t\t\t<-------LITERAL TABLE--------->\n\n")
    print("\t\t\t  line no    literal count      literal value")
    for i in range(len(Literal)):
        for j in range(len(Literal[i])):
            print("\t\t\t\t", Literal[i][j], end="")
        print()
