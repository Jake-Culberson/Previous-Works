#include <msp430.h> 

float Brightness=50.0;
int main(void)
{
    WDTCTL = WDTPW + WDTHOLD;    // stop watchdog timer


    _EINT();        //Global interrupt

    P1DIR |= BIT0;  //set LED 1.0 as an output

    P2SEL |=BIT4;   //P2.4 pin function

    P2DIR |= BIT4;  //Set P2.4 as an output


    TA2CCR0 = 1000;
    TA2CCR1 = 500;
    TA2CCTL1 |= OUTMOD_6;


    TA2CTL = TASSEL_2 | MC_3;   //set program to up/down mode and use SMCLK

    //set switch 1 and 2 and their I/O's
    P1DIR &= ~(BIT1);
    P2DIR &= ~(BIT1);

    P2OUT |= BIT1;
    P1OUT |= BIT1;

    //S1 setup
    P2REN |= BIT1;
    P2IFG &= ~BIT1;

    P2IE |= BIT1;//enables the interrupt
    P2IES |= BIT1;


    //S2 setup
    P1REN |=BIT1;
    P1IFG &= ~BIT1;

    P1IE |=BIT1;//enables the interrupt
    P1IES |= BIT1;

    _BIS_SR(LPM0_bits + GIE);//LPM
}


#pragma vector = PORT1_VECTOR //allows SW2 to lower the brightness
interrupt void PORT1_ISR(void)
{
    P1IFG &= ~(BIT1); //clear flags

    if((P1IN&BIT1)==0x00){//checks if button 2 is pressed

        _delay_cycles(10000); //debounce
        if((P1IN&BIT1)==0){

                if(Brightness > 0){  //makes sure the brightness wont go over max and loop

                    Brightness -= 12.5;//changes the int so that the previous if check can be effective
                    TA2CCR1 += 125;//increases brightness

                }

            }
        while (((P1IN&BIT1)==0x00) && ((P2IN&BIT1)==0x00)) {


            _delay_cycles(3000000);
            TA2CCR1 = 1000;
            _delay_cycles(3000000);
            TA2CCR1 = (100 - Brightness) * 10;
            P2IFG &= ~(BIT1); //clear flags
                    }
    }


}

#pragma vector = PORT2_VECTOR//allows SW1 to increases brightness
interrupt void PORT2_ISR(void)
{
    P2IFG &= ~(BIT1); //clear flags
    if((P2IN&BIT1)==0x00){//checks if button 1 is pressed

        _delay_cycles(10000); //debounce
        if((P2IN&BIT1)==0){//checks if button is pressed

                if(Brightness < 100.0){//makes sure the brightness wont go over min and loop

                    Brightness += 12.5;//changes the int so that the previous if check can be effective
                    TA2CCR1 -= 125;//decreases brightness
                }
        }
        while (((P1IN&BIT1)==0x00) && ((P2IN&BIT1)==0x00)) {


            _delay_cycles(3000000);
            TA2CCR1 = 1000;
            _delay_cycles(3000000);
            TA2CCR1 = (100 - Brightness) * 10;

            P2IFG &= ~(BIT1); //clear flags
                    }
    }
}













