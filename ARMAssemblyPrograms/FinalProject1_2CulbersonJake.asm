;Jake Culberson
;CPE-221-01
;Final Project Sieve of Eratosthenese
;
;
;
;void sieve(bool isPrime[], int n) {
;	for (int i = 2; i <= n; ++i) {
;		isPrime[i] = true;
;	}
;	
;	isPrime[0] = false; 0 and 1 arent primes
;	isPrime[1] = false;
;	
;	//this section will flag all composites as not prime 
;	for (int i = 2; i * i <= m; ++i) {
;	if (isPrime[i]) {
;		for (int j = i * i <= n; j += i) {
;			isPrime[j] = false;
;			}
;		}
;	}
;}
;
;int main() {
;	int n = 541;
;	bool isPrime[n + 1];
;	sieve(isPrime, n)
;	//after the array is created this will iterate through the array and print the prime numbers
;	for (int i = 0; i <= n; ++i) {
;	if (isprime[i]) {
;		cout << i << " "; // gives every prime in a row
;		}
;	}
;	cout << endl;
;	return 0;
;}//end of C++ program
;
;
;The Flags are at 0x000000C0-0x00000930
;I put my memory map range as 0x00000000-0x00002000 to give alot of room
;
;

		AREA FinalPorject1_2, CODE, READWRITE	
		ENTRY

MAIN
		LDR R0, i				;load address of i into R0
		LDR R1, CounterOne		;load address of CounterOne into R0
		LDR SP, PointerOne		;load stack pointer with address of PointerOne
		BL	PrimeSieve			;using PrimeSieve like a function
Done	B 	Done				;end of program



PrimeSieve
		MOV 	R2, #2			;Set R2 to 2

CompRemove
		ADR 	R3, comprime	;laod address of comprime into R3
		PUSH	{R0}			;Push R0 onto stack
		CMP	 	R2, #25			;compare R2 with 25
		BEQ		RemDone			;branch if R2 = 25
		LDR 	R0, [R3, R2, LSL #2] ;load number from memory
		CMP 	R0, #0			;checks the flags
		POP		{R0}			;pop value from stack to R0
		PUSH	{R0}			;Push R0 to the stack
		BEQ		PrimeCheck		;if R0 = 0 its prime if not its composite
		BGT		CompCheck		;skips storing R0 if R0 does not equal the flag 0
		

PrimeCheck
		BL		Sieve			;use sieve liek a function
CompCheck
		POP 	{R0}			;pop vlaue from stack to R0
		ADD 	R2, R2, #1		;increase R2 By 1
		B CompRemove			;loops back to compremove



RemDone
		POP		{R0}			;Pop value from memory
		MOV 	R0, #2			;puts the value 2 into R0
		
		;pushes R2 and R3 onto the stack to save them.
		PUSH	{R2}			
		PUSH	{R3}
		;loads the result and comprime stacks
		ADR		R3, result 
		ADR		R2, comprime
repeatOne
		LDR		R1, CounterOne	;loads address of counterone into R1
		CMP		R0, R1			;compares the counter with the iterator i
		BGE 	Done			;if the iterator is greater than or equalt to counterone itll branch out
		
		LDR 	R1, [R2, R0, LSL #2];Load number from comprime
		CMP		R1, #0			;compares R1 to 0 to determine if the flag is set or not
		BGT		Composite		;if the flag is 1 then it will not store the value because only composites have 1
		
		
		STR		R0, [R3], #4	;stores values to the result array
Composite
		ADD		R0, R0, #1		;iterate i
		B		repeatOne		;loops the inner repeat
		



;the actual sieving part of the sieve or erotoestheneneneeezz
Sieve
		;Squares R2 and puts it into R0
		;the reason being so that the flagger will start in the most optimal spot
		;2*2 starts at 4 leaving the prime 2 intact, and iterates through all numbers
		;3*3 starts at 9 which would be concerning because the composites 6 and 8 would be missed, 
		;but those 2 composites would have been already checked by the first loop of 2's
		;4*4 is 16 which misses 10,12,14,15, each of which are already caught by 2 and 3
		;and so the cycle continues
		MUL		R0, R2, R2		
miniSieve
		LDR		R1, CounterOne	;loads counterone
		CMP		R0,	R1			;compares R0 to the counter
		BGT		SieveDone		;if the iterator I is larger than the counter
		
		MOV		R1, #1			;creates the flag to set composites
		STR		R1, [R3, R0, LSL #2];stores 1 to act as a flag for the composites
		ADD		R0, R0, R2		;iterates further
		B		miniSieve		;loops back to minisieve so all composites are caught until it breaks out
SieveDone
		BX		LR				;branches back to where BL was written like a function should

;Data area
i			DCD 	2
CounterOne 	DCD		542
PointerOne	DCD		196 ;the stack values are at 0x000000BC-0x000000C0
comprime	SPACE	2172;The Flags are at 0x000000C0-0x00000930
result		SPACE	400 ;The Result values are at 0x00000934-0x00000AC4
endmark		DCD		10  ;The end mark is at 0x00000AC8
		END