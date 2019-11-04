import re
import Object_pyc as OP

symbol = list()

def Symbol_Table_File():
    f = open("File.asm", "r")
    line = f.readlines()
    no = 0
    sy = 0
    addr = 0
    for i in line:
        no += 1
        str1 = (re.split(r'[.:,\s]\s*', i))

        if str1[0] == "section":
            addr = 0000

        elif OP.check_Data_Section(str1[2]):
            data1 = list()
            if OP.Repate_variable(no, str1[1], symbol):
                c = 0
                sy += 1
                data1.append(no)
                data1.append(sy)
                data_lst = ""
                for i in range(len(str1)):
                    if str1[i] != "":
                        if i == 1:
                            data1.append(str1[i])
                            data1.append("data")
                            data1.append("D")
                        elif i == 2:
                            data1.append(str1[2])

                    if i > 2:
                        if str1[i] != "":
                            data_lst += str1[i] + " "
                            c += 1

                if str1[2] == "db":
                    c = len(data_lst) - 3
                size = OP.Check_data_size(str1[2]) * c
                data1.append(addr)
                addr += size
                data1.append(size)
                data1.append(data_lst)
                value_addr = OP.Return_Addr_id(data_lst)
                data1.append(value_addr)
                symbol.append(data1)


        elif OP.Check_Bss_Section(str1[2]):
            data2 = list()
            if OP.Repate_variable(no, str1[1], symbol):
                sy += 1
                data2.append(no)
                data2.append(sy)
                for i in range(len(str1)):
                    if str1[i] != "":
                        if i == 1:
                            data2.append(str1[i])
                            data2.append("bss")
                            data2.append("D")
                        elif i == 2:
                            data2.append(str1[i])
                size = OP.Check_bss_size(str1[2]) * int(str1[3])
                data2.append(addr)
                addr += size
                data2.append(size)
                data2.append("-")
                data2.append("-")
                symbol.append(data2)

        elif str1[1] == "extern" or str1[1] == "global":
            for e in range(2, len(str1)):
                if OP.Repate_variable(no, str1[1], symbol):
                    data3 = list()
                    data3.append(no)
                    if str1[e] != "":
                        sy += 1
                        data3.append(sy)
                        data3.append(str1[e])
                        data3.append("txt")
                        if str1[2] == "main":
                            data3.append("D")
                        else:
                            data3.append("U")
                        for k in range(5):
                            data3.append("-")
                        symbol.append(data3)

        elif OP.Check_Opcode(str1[1]):
            data4 = list()
            if OP.Repate_variable(no, str1[0], symbol):
                if str1[0] != "":
                    sy += 1
                    data4.append(no)
                    data4.append(sy)
                    data4.append(str1[0])
                    data4.append("txt")
                    data4.append("U")
                    data4.append("Label")
                    for k in range(4):
                        data4.append("-")
                    symbol.append(data4)

                if ~(OP.Check_Reg(str1[2])):
                     OP.Check_variable(str1[2], symbol)

        else:
            if ~OP.check_Data_Section(str1[2]) or ~OP.Check_Bss_Section(str1[2]) or ~OP.Check_Opcode(str1[1]):
                OP.ERROR.append("text.asm:{}: error: parser: instruction expected".format(no))


    if len(OP.ERROR) != 0:
        for i in range(len(OP.ERROR)):
            print(OP.ERROR[i])
        return
    print("\n\t\t\t\t\t\t\t\t\t\t<---SYMBOL TABLE--->\n\n")
    print("\t   line number\t\tSym_no\t   Sym_name\t\t  section     Define/undefine   data_type    strt_adr   size\t\tvalue")
    for i in range(len(symbol)):
        for j in range(len(symbol[i])-1):
            print("\t\t\t", symbol[i][j], end="")
        print()
#Symbol_Table_File()