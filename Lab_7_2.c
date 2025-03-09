#include <msp430.h> 

int BUZZERON = 0;


//main.c
int main(void)
{
    WDTCTL = WDT_ADLY_1000;

    P8DIR |= BIT1;  //Setting p8.1 as output
    P8OUT &= ~BIT1;

    TB0CCR0 = 8;    //sets the cycle to be a 2Khz signal

    TB0CCTL0 |= CCIE;   //Enable timer interrupts

    TB0CTL = TBSSEL_1+MC_1;    // set the program to up mode and ACLK

    SFRIE1 |= WDTIE;
    _EINT();

    _BIS_SR(LPM0_bits + GIE); //LPM
    return 0;
}

#pragma vector = WDT_VECTOR
interrupt void watchdog_timer(void)
{
    TB0CCTL0 ^= CCIE;       //Toggle interrupt for TB0
}

#pragma vector = TIMERB0_VECTOR
interrupt void timerISR2(void)
{
    P8OUT^=BIT1;    //run P8.1 to release the 2KHz
}







