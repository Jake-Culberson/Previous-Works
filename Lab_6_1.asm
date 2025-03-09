;-------------------------------------------------------------------------------
; MSP430 Assembler Code Template for use with TI Code Composer Studio
;
;
;-------------------------------------------------------------------------------
            .cdecls C,LIST,"msp430.h"       ; Include device header file
            
;-------------------------------------------------------------------------------
            .def    RESET                   ; Export program entry-point to
                                            ; make it known to linker.
			.def Interrupt_2
			.def Interrupt_1
;-------------------------------------------------------------------------------
            .text                           ; Assemble into program memory.
            .retain                         ; Override ELF conditional linking
                                            ; and retain current section.
            .retainrefs                     ; And retain any sections that have
                                            ; references to current section.

;-------------------------------------------------------------------------------
RESET       mov.w   #__STACK_END,SP         ; Initialize stackpointer
StopWDT     mov.w   #WDTPW|WDTHOLD,&WDTCTL  ; Stop watchdog timer


;-------------------------------------------------------------------------------
; Main loop here
;-------------------------------------------------------------------------------

main:
	;sets the LED------------------
	bis.b #0x01,&P1DIR
	bis.b #0x80,&P4DIR
	;------------------------------

	;set the button inputs---------
	bic.b #0x02,&P2DIR
	bis.b #0x02,&P2REN
	bis.b #0x02,&P2OUT

	bic.b #0x02,&P1DIR
	bis.b #0x02,&P1REN
	bis.b #0x02,&P1OUT
	;-------------------------------

	;turns the LED's on as an initial state
	bis.b #0x01,&P1OUT
	bis.b #0x80, &P4OUT
	;-------------------------------

	;enable Global interupts
	bis.w #GIE,SR
	;-------------------------------

	;falling edge trigger for the switches
	bis.b #0x02,&P1IE
	bis.b #0x02,&P1IES
	bic.b #0x02,&P1IFG
	;-------------------------------


	bis.b #0x02, &P2IE
	bis.b #0x02, &P2IES
	bic.b #0x02, &P2IFG
	mov.w #0,R13

innerloop:
		jmp $

;subroutine for switch 2

;reset flags
Interrupt_2: bic.b #0x02,&P1IFG

;check if button is pressed
CheckSW2: bit.b #0x02,&P1IN
		jnz endof


;delay for the lights
debounce2: mov.w #1000,R15
blink2: dec.w R15

	      nop
	      nop
	      nop
	      nop
	      nop
	      nop
	      nop

	      jnz blink2
	      bit.b #0x02,&P1IN
	      jnz endof
	      mov.w #7,R14
loopinit: mov.w #50000,R15
		  xor.b #0x01,&P1OUT
loopstart:
		  dec.w R15

		  nop
		  nop
		  nop
		  nop
		  nop
		  nop
		  nop

		  jnz loopstart
		  xor.b #0x01,&P1OUT

		  mov.w #50000,R15
		  dec.w R14

		  jnz loopstart
		  xor.b #0x80,&P4OUT
BRelease2: bit.b #0x02,&P1IN
		  jz BRelease1
endof:	reti




;subroutine for switch 1

;reset flags
Interrupt_1: bic.b #0x02,&P2IFG

;check if button is pressed
checksw1: bit.b #0x02,&P2IN
		  jnz Tloope

debounce1:mov.w #1000,R15
blink1: dec.w R15

		  nop
		  nop
		  nop
		  nop
		  nop
		  nop
		  nop

		  jnz blink1
		  bit.b #0x02,&P2IN

		  jnz Tloope
		  xor.b #0x80,&P4OUT

BRelease1:bit.b #0x02,&P2IN
		 jz BRelease1
Tloope:		reti




            .global __STACK_END
            .sect   .stack
            

            .sect   ".reset"
            .short  RESET
            .sect ".int47"
            .short Interrupt_2
            .sect ".int42"
            .short Interrupt_1
