; hayneko_arch32S

; Simple test program for the hayneko_arch32S architecture

#entry main

.init ST
		;
.init FI

main:
	IMMB	ra, 0x00
	MOV	rd, ra
	IMMB	rc, 0x3F

	REP:
		ADD	ra, ra, rd
		DEC	rc
		JNZ	REP
		J	FINISH

	FINISH:
		C	print_msg
		RET

print_msg:
	IMMB	rd, 0x48
	IMMDW	r8, 0x0000003C
	SYSCALL
	XOR	rd, rd, rd
	IMMB	r8, 0x0A
	SYSCALL
	RET

; optimize this file:
; MOV ra, x0
; MOV rd, x0
; IMMB rc, 0x3F
; REP:
;   ADD ra, ra, rd
;   DEC rc
;   JNZ REP
;   IMMB rd, 0x48
;   IMMDW r8, 0x0000003C
;   SYSCALL
;   XOR rd, rd, rd
;   IMMB r8, 0x0A
;   SYSCALL
;   RET
; 
; complied to binary:
; 
; 00000000: 01 10 01 50 4F 02 3F 02 01 15 02 A3 4B 07 00 4F
; 00000010: 50 48 43 90 00 00 00 0A 3C 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 
; 