#include <msp430.h> 


/**
 * main.c
 */
unsigned int EightMhz = 0;
unsigned int FourMhz = 0;
unsigned int TwoMhz = 0;
unsigned int OneMhz = 1;
int main(void)
{
    WDTCTL = WDTPW + WDTHOLD;   // stop watchdog timer


    P1DIR |= BIT0;  //SMCLK Set out to pins
    P1OUT = 0x00;

    P4DIR |= BIT7;  //MCLK set out to pins
    P4OUT = 0x80;

    _EINT();
    P2DIR &= ~BIT1;
    P2REN |= BIT1;
    P2OUT |= BIT1;
    P2IFG &= ~BIT1;
    P2IE |= BIT1;
    P2IES |= BIT1;

    P1DIR &= ~BIT1;
    P1REN |= BIT1;
    P1OUT |=BIT1;
    P1IFG &=~BIT1;
    P1IE |=BIT1;
    P1IES |= BIT1;

    UCSCTL3 = SELREF_2;
    UCSCTL4 |= SELA_2;
    UCSCTL0 = 0x0000;
    do
    {
        UCSCTL7 &= ~(XT2OFFG+XT1LFOFFG+DCOFFG);
        SFRIFG1 &= ~OFIFG;
    } while(SFRIFG1&OFIFG);
    unsigned int i = 0;
    while(1)
    {
        for(i=0;i<50000;i++);
            P1OUT ^=0x01;
            P4OUT ^= 0x80;

    }
    return 0;
}

#pragma vector = PORT2_VECTOR
__interrupt void PORT2_ISR(void)
{
    P2IFG &=~BIT1;

    _delay_cycles(20000);
    if((P2IN&BIT1) !=0x00)
    {
        return;
    }
    __bis_SR_register(SCG0);
    if(EightMhz==1)
    {
        UCSCTL1 = DCORSEL_3;
        UCSCTL2 = 124;
        EightMhz =0;
        FourMhz = 1;
        __bic_SR_register(SCG0);


        _delay_cycles(125000);

    }
    else if(FourMhz==1)
    {
        UCSCTL1 = DCORSEL_3;
        UCSCTL2 =  62;
        FourMhz =0;
        TwoMhz = 1;
        __bic_SR_register(SCG0);

        _delay_cycles(62500);

    }
    else if(TwoMhz ==1)
    {
        UCSCTL1 = DCORSEL_3;
        UCSCTL2 = 32 ;
        TwoMhz = 0;
        OneMhz = 1;
        __bic_SR_register(SCG0);

        _delay_cycles(31250);

    }
    return;

}

#pragma vector = PORT1_VECTOR
__interrupt void PORT1_ISR(void)
{
    P1IFG &=~BIT1;

    _delay_cycles(20000);
    if((P1IN&BIT1)!=0x00)
    {
        return;
    }
    __bis_SR_register(SCG0);
        UCSCTL1=DCORSEL_5;
        UCSCTL2 = 249;
        __bic_SR_register(SCG0);
        __delay_cycles(250000);
        EightMhz = 1;
        OneMhz =0;
        return;
}
