

		AREA Assembly_Project_1_1, CODE, READWRITE
        ENTRY

		adr		R0, x;
		adr 	R1, y;
		adr		R2, z; loads the base address of z into R4
		ldr 	R3, size; gives the loop count
		ldr		R4, i; starts the loop counter at 0

Loop	cmp		R4, R3; compares the loop counter to the amount of times it has iterated
		bge 	BDone; when the loop counter has reached the desired amount the project 
				; jumps to the end of the program
		ldr 	R5, [R0]; Loads X[i] into R0
		ldr		R6, [R1]; Loads Y[i] into R1

		cmp		R5, R6; Compares X[i] and Y[i]
		
		ble		LeEq; Breaks if X[i] is <= y[i]

		str 	R5,[R2]; if X[i] > Y[i] store X[i] to Z[i]
		B		ItLoop; used to skip over LeEq

LeEq	str 	R6,[R2]; If X[i] > Y[i] store Y[i] to Z[i]


ItLoop	

		add		R0, R0, #4
		add		R1, R1, #4
		add		R2, R2, #4
		add 	R4, R4, #1; simply iterates the loop counter to the next iteration


		B		Loop; loops back to the top

BDone	B	BDone

size 	dcd 10
i		dcd 0
x		dcd 100, 3, -1, 2, 4, 4, 2, -1, 3, 100
y		dcd -53, 247, 95, -7, 481, 91, -33, 1500, 29, -83
z		space 40

		align 2;
	
		END
;label to end the project

	
	
	