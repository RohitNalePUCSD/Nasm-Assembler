section .data
    num1 db   "This is the string",10,0
    num2 dd   10,20
section .bss
    num3 resb 1
    num4 resb 2
section .text
    global main
    extern print,msg
main:mov eax,100
    mov ebx,200
abc:add eax,10
    jmp abc
pqr:mov eax,50
