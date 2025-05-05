from inlineasm import asm

def my_add():
    asm("""
    mov eax, [ebp + 8]
    add eax, [ebp + 12]
    ret
    """)
result = my_add(2, 3)
print("Resultado:", result)