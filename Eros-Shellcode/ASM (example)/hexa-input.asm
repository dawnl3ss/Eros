xor eax, eax
xor ebx, ebx
xor edx, edx
jmp short string
code:
pop ecx
mov bl,1
mov dl,23
int 0x80
dec bl
mov al,1
int 0x80
string:
call code
db 'thats an example for an assembly code'
