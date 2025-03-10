



;Memory Map 0x00000000, 0x000000BB

		AREA Assembly_Project_2, CODE, READWRITE
		ENTRY


		adr		R0, x;
		adr 	R1, y;
		adr		R2, e; loads the base address of z into R4
		ldr 	R3, size; gives the loop count
		ldr		R4, i; starts the loop counter at 0
		
Loop
    ; Check loop termination condition
    CMP     R4, R3
    BGE     BDone

    ; Load index value from array x, and y
    LDR     R5, [R0]
	LDR		R6, [R1]
	
	CMP 	R5,#0
	BPL		XLEnd
	BL		Xloop
	
XLEnd

	CMP		R6,#0
	BPL 	YLEnd	
	BL		Yloop
YLEnd

	CMP		R5, R6
	BL		Wloop
	
WLDone
	
	STR 	R6,[R2]		;because it is a common denominator it doesntmatter
			

	ADD		R0, R0, #4
	ADD		R1, R1, #4
	ADD 	R2, R2, #4
	
	ADD     R4, R4, #1; Increment loop counter

	
	
    b       Loop; Repeat loop
	
	   ; Define arrays x, y, and z
	   
Xloop	
	
	SUB R5, R5, R5, LSL#1
	bx		LR

Yloop

	SUB R6, R6, R6, LSL#1
	bx		LR
	   
Wloop	

	CMP	R5, R6
	BEQ 	WLDone
	BGT		XGY	
	SUB R6,R6,R5
	B		Wloop
	
XGY
	SUB R5,R5,R6
	B		Wloop
	   
	   
BDone	b	BDone

size 	dcd 4
i		dcd 0
x       dcd -8, -295, 280, 81 
y       dcd 9, -45, 8, -243
e       space 16

    ; End of program
    END

