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