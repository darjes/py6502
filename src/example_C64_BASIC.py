# This shows how to simply feed in straight text
# by passing it through splitlines()

from asm6502 import asm6502

code = """
        ORG  $100
start:
        LDA #$10
        LDX #$00
loop:
        STA $1000,x
        INX
        SBC #$01
        BPL loop
        RTS
"""

lines = code.splitlines()

a = asm6502()
(l,s) = a.assemble(lines)
for line in l:
    print (line)
print
for line in s:
    print (line)

# Memory dump for BASIC
memory = []
for dec in a.object_code[256:]:
    if(dec == -1):
        break
    memory.append(dec)
        
print("\n\nMemory Dump:", memory)
print("Length:", len(memory), "bytes")
