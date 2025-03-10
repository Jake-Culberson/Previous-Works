

		AREA Assembly_Project_1_2, CODE, READWRITE
		ENTRY

		adr		R0, x;
		adr 	R1, y;
		adr		R2, z; loads the base address of z into R4
		ldr 	R3, size; gives the loop count
		ldr		R4, i; starts the loop counter at 0
		
Loop
    ; Check loop termination condition
    CMP     R4, R3
    BGE     BDone

    ; Load index value from array x
    LDR     R5, [R0]
	MOV 	R5, R5, LSL#2

    ; Load value from array y using index from array x
    ADD     R6, R1, R5
	LDR 	R6, [R6]

    ; Store value from y into array z
    STR     R6, [R2]

    ADD     R4, R4, #1; Increment loop counter
	ADD		R0, R0, #4;
	ADD 	R2, R2, #4;
	
    b       Loop; Repeat loop
	
	   ; Define arrays x, y, and z
BDone	b	BDone

size 	dcd 10
i		dcd 0
x       dcd 0, 1, 3, 6, 2, 5, 8, 7, 4, 9
y       dcd -53, 247, 95, -7, 481, 91, -33, 1500, 29, -83
z       space 40

    ; End of program
    END