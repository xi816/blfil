section .data
  tt: db "Hello World!", 10
  lt: equ $-tt

section .text
  global _start

_start:
  mov eax, 4
  mov ebx, 1
  mov ecx, tt
  mov edx, lt
  int 80h

  mov eax, 1
  mov ebx, 0
  int 80h

