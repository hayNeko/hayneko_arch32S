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

## Hayneko_Arch32S interrupt vectors

there are total 256 interrupt vectors available in Hayneko_Arch32S. The interrupt vectors are located at the beginning of the memory space. The interrupt vectors are used to handle interrupts and exceptions.

`*` means the interrupt vector needs a very high priority to be handled.\
`#` means the interrupt vector is a non-maskable interrupt (NMI) vector.\
`~` means the interrupt vector is a maskable interrupt (INT) vector.

```txt
~DE     : Divided Error, triggered when a division by zero or overflow occurs during integer division. (It can be masked.)

#UD     : Undefined Instruction, triggered when an invalid or undefined opcode is encountered during instruction decoding. (It cannot be masked.)

*ABORT  : Abort, A critical error that causes the processor to halt execution and enter a safe state, often used for severe hardware or software failures. (It may be handled in L7(Platform Secure mode, the highest priority level))
```
