# HAYNEKO ARCH32S Documentation
The HAYNEKO ARCH32S is a 32-bit architecture designed for efficiency and performance in embedded systems. This documentation provides an overview of its features, instruction set, and architecture specifics.



## Hayneko_Arch32S instruction length types

- instruction starts with `00`:
    - 1 to 2 bytes instruction length
    - 1 byte or no operand
    - usually a control, stack or single byte arithmetic instruction
- instruction starts with `01`:
    - 3 to 4 bytes instruction length
    - 1 to 3 bytes operand
    - usually a short immediates or 2-3 register instructions
- instruction starts with `10`:
    - 5 to 8 bytes instruction length
    - 1 to 7 bytes operand
    - usually a long immediates or 4-8 register instructions
- instruction starts with `11`:
    - it is a **prefix** or **extended opcode** instruction
    - 1 byte length
    - no operand
    - instrucion decoder will decode the next instruction based on the prefix

### Hayneko_Arch32S instruction prefixes

- prefixes start with `11` and are used to extend/change the instruction behavior
- one instruction can have multiple prefixes, following a fixed order
- some of the prefixes conflict with each other, and the instruction decoder will ignore the conflict
    - `REX` and `FEX` prefixes conflict with each other, only one of them can be used in an instruction

- `REX` and `FEX` prefixes are used to extend the register operand of the instruction
    - for `REX` prefix, the range of registers is extended from 0-15 to 16-31
    - for `FEX` prefix, the range of registers is extended from single-precision to double-precision

- `BRH-H` prefix provides a branch hint to the instruction decoder
    - it can improve the branch prediction performance
    - it can only be used with conditional branch instructions, otherwise it will be ignored


## Hayneko_Arch32S interrupt vectors

there are total 256 interrupt vectors available in Hayneko_Arch32S. The interrupt vectors are located at the beginning of the memory space. The interrupt vectors are used to handle interrupts and exceptions.

`*` means the interrupt vector needs a very high priority to be handled.\
`#` means the interrupt vector is a non-maskable interrupt (NMI) vector.\
`~` means the interrupt vector is a maskable interrupt (INT) vector.

```plain text
~DE     : Divided Error, triggered when a division by zero or overflow occurs during integer division. (It can be masked.)

#UD     : Undefined Instruction, triggered when an invalid or undefined opcode is encountered during instruction decoding. (It cannot be masked.)

*ABORT  : Abort, A critical error that causes the processor to halt execution and enter a safe state, often used for severe hardware or software failures. (It may be handled in L7(Platform Secure mode, the highest priority level))
```
