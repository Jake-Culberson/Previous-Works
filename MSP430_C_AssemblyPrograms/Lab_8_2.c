


#include <msp430.h>
/**
* main.c
*/
void UART_SETUP(void)
{
     P3SEL |= BIT3+BIT4;
     UCA0CTL1 |= UCSWRST; //reset
     UCA0CTL0 = 0; //USCI_A0 control register
     UCA0CTL1 |= UCSSEL_2; //SMCLK source
     UCA0BR0 = 18; //1048576 Hz
     UCA0BR1 = 0x00; //upper byte
     UCA0MCTL = 0x02;
     UCA0CTL1 &= ~UCSWRST; //clear reset
}



void UART_putCharacter(char c)
{
     while((UCA0IFG&UCTXIFG)==0);
     UCA0TXBUF = c;
}


int main(void)
{
    // WDTCTL = WDT_ADLY_1000;
     WDTCTL = WDTPW + WDTHOLD; // stop watchdog timer
    UART_SETUP();
    volatile float data;


    unsigned int i;
    unsigned int j;
    unsigned int k;
    unsigned int counterOne=0; //determines number of up/downs on wave
    unsigned int stop=0; //if set to 1 will stop loop
    unsigned int mode =0; //changes the mode to either up or down if value is 0 or 1
    char* byt = (char*) &data;
    data = 0;
    UART_putCharacter(0x55);
    for(k=0;k<4;k++)
     {
        UART_putCharacter(byt[i]);
     }
    while(stop!=1)
        {
         unsigned int i; //counter index variables
         unsigned int j;
         if(mode == 0)
         {
             data+=0.04;
             UART_putCharacter(0x55);
             for(i=0;i<4;i++)
             {
                 UART_putCharacter(byt[i]);

             }
             if(data>=8)
             {
                 mode=1;
                 counterOne++;
             }
         }
         else if(mode == 1)
         {
             data=data-0.04;
             UART_putCharacter(0x55);
             for(j=0;j<4;j++)
             {
                 UART_putCharacter(byt[j]);
             }
             if(data<=0)
             {
                 mode=0;
                 counterOne++;
             }
         }
         if(counterOne==8)
         {
             stop=1; //stop program
         }
    }
    while(1); //freezes program
    return 0;
}


