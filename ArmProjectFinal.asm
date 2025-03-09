
		AREA ArmProjectFinal, CODE, READWRITE
		ENTRY    

MAIN        
;		LDR   SP
		LDR   R0, i	            	
		ADR   R2, result            
		BL    Sieve                 
DONE	B     DONE                  

Sieve
		PUSH{LR}
notaprime
		ADD R0, R0, #1
		MOV R1, R0
repeatOne	
		SUB R1, R1, #2
		CMP R1, #2
		BGT		repeatOne
		BEQ		notaprime
		MOV R1, R0
		
repeatTwo
		SUB R1, R1, #3
		CMP R1, #3
		BGT		repeatTwo
		BEQ		notaprime
		MOV R1, R0
		
repeatThree
		SUB R1, R1, #5
		CMP R1, #5
		BGT		repeatThree
		BEQ		notaprime
		MOV R1, R0
		
repeatFour
		SUB R1, R1, #7
		CMP R1, #7
		BGT		repeatFour
		BEQ		notaprime
		MOV R1, R0
		
repeatFive
		SUB R1, R1, #11
		CMP R1, #11
		BGT		repeatFive
		BEQ		notaprime
		MOV R1, R0
		
repeatSix
		SUB R1, R1, #13
		CMP R1, #13
		BGT		repeatSix
		BEQ		notaprime
		MOV R1, R0
		
repeatSeven
		SUB R1, R1, #17
		CMP R1, #17
		BGT		repeatSeven
		BEQ		notaprime
		MOV R1, R0

repeatEight
		SUB R1, R1, #19
		CMP R1, #19
		BGT		repeatEight
		BEQ		notaprime
		MOV R1, R0

repeatNine
		SUB R1, R1, #23
		CMP R1, #23
		BGT		repeatNine
		BEQ		notaprime
		STR R0, [R2, R3, LSL #2]
		PUSH {R0}
		ADD R3, R3, #1
		CMP R3, #100
		BLT		notaprime
		POP {PC}
		
		B 		DONE

		
result     	SPACE    	400         ; Space for storing the result
endmark    	DCD      	10          ; End mark
i			DCD		 	1
j			DCD			0
			END