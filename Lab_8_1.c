


#include <msp430.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* marketbot = "\x1b[36mMarket Bot: \x1b[m";
char* messageOne = "Hi I am Market Bot. What is the name for your Order?";
char* usertxt = "\x1b[33mUser: \x1b[m";
char* food = "Today we have eggs, chicken, and milk. What Would you like to order?";

void UART_SETUP(void)

{
     P3SEL |= BIT3+BIT4;
     UCA0CTL1 |= UCSWRST; //reset
     UCA0CTL0 = 0; //USCI_A0 control register
     UCA0CTL1 |= UCSSEL_2; //SMCLK source
     UCA0BR0 = 0x09; //lower byte
     UCA0BR1 = 0x00; //upper byte
     UCA0MCTL = 0x02; //Modulation (UCBRS0=0x01,UCOS16=0)
     UCA0CTL1 &= ~UCSWRST; //Clearing the software reset for init of USCI state
}



void UART_sendChar(char bip)
{
     while((UCA0IFG&UCTXIFG)!=UCTXIFG); //while transmit buffer is not free, wait until it is
     UCA0TXBUF = bip;
}




char UART_getChar(void)
{
     while((UCA0IFG&UCRXIFG)!=UCRXIFG); //If a char has not been received in buff wait until one is
     UART_sendChar(UCA0RXBUF); //echo character
     return UCA0RXBUF;
}





void UART_sendString(char* str)
{
     int counterOne = 0;
     while(1)
     {
         while((UCA0IFG&UCTXIFG)!=UCTXIFG); //waiting for buffer to be free

         if(str[counterOne]==0)
         {
             break;
         }
         else
         {
             UART_sendChar(str[counterOne]);
             counterOne++;
         }
     }
}



void UART_getLine(char* buff,int limit)
{
     int counterOne = 0;
     char temp = 0; //just an initial value
     while(counterOne<(limit-1) && temp != '\r') //If limit-1 is reached, this loop needs to stop
     { //space has to be saved for a nul char
     //This means at char 49 (counterOne 48) loop will stop
     //giving one more index position for a null char
         temp = UART_getChar();
         if((temp!='\b') && (temp!='\r') && (temp!=127))
         {
             buff[counterOne] = temp;
             counterOne++;
         }
         else if((temp=='\b') || (temp==127))
         {
             counterOne--;
         }
     }
     if(counterOne==(limit-2))
     {
         buff[(limit-1)]= 0; //null char for last counterOne
     //if characters exceed limit
     }
     else if(temp=='\r')
     {
         buff[counterOne] = 0;
     }
}



void nextline(void) //function specifically meant to just go to the next line
{
     UART_sendChar('\r'); //returns to first character in a line
     UART_sendChar('\n'); //goes to the next line. Basically getting ready for new txt
}

int CheckItem(char* itemName)
{
     unsigned int CIfBlank= 0; //checks all values to see which was chosen by comapring the string
     unsigned int counterTwo = 0;
     while(itemName[counterTwo]!=0)
     {
         itemName[counterTwo]=tolower(itemName[counterTwo]);
         counterTwo++;
     }


     while(CIfBlank==0)
     {
         if(strcmp(itemName,"eggs")==0)
         {
             CIfBlank = 1;
             UART_sendString(marketbot);
             UART_sendString("eggs cost $2 each dozen. How many would you like?\r\n");
             return 1;
         }
         else if(strcmp(itemName,"chicken")==0)
         {
             CIfBlank = 1;
             UART_sendString(marketbot);
             UART_sendString("chicken cost $1 per pound. How many would you like?\r\n");
             return 2;
         }
         else if(strcmp(itemName,"milk")==0)
         {
             CIfBlank =1;
             UART_sendString(marketbot);
             UART_sendString("milk cost $2 each gallon. How many would you like?\r\n");
             return 3;
         }
         else
         {
             UART_sendString(marketbot);
             UART_sendString(itemName);
             UART_sendString(" are not available today.\r\n");
             UART_sendString(marketbot);
             UART_sendString(food);
             UART_sendString("\r\n");
             return 0;
         }
     }
}





int main(void)
{
    WDTCTL = WDTPW + WDTHOLD; // stop watchdog timer
    UART_SETUP();
    char buffer[30];


    //base strings
    // char* marketbot = "Market Bot: ";
    // char* messageOne = "Hi I am Market Bot. What is the name for your Order?";
    // char* usertxt = "User: ";

    char username[30]; //a name shouldnt be longer than 30 characters so i set the maximum allowable name to that

    //Values of individual items and a sale counter
    unsigned int sale;
    unsigned int addItem;
    unsigned int itemTotal;
    while(1)
    {
         sale = 0;
         addItem = 1;

         //asks for name and starts the program
         UART_sendString(marketbot);
         UART_sendString(messageOne);
         UART_sendString("\r\n");

         //User responds with name
         UART_sendString(usertxt);
         UART_getLine(username,30);
         UART_sendString("\r\n");


         //gives the cordial response and asks the question

         UART_sendString(marketbot);
         UART_sendString("Hello ");
         UART_sendString(username);
         UART_sendString("!\r\n");
         while(addItem==1)
         {
             //first order
             UART_sendString(marketbot);
             UART_sendString(food);
             UART_sendString("\r\n");


             UART_sendString(usertxt);
             UART_getLine(buffer,30); //getting the item that the user requests
             UART_sendString("\r\n");


             unsigned int Result = CheckItem(buffer);
             while(Result==0)
             {

                 UART_sendString(usertxt);
                 UART_getLine(buffer,30);
                 UART_sendString("\r\n");
                 Result = CheckItem(buffer);
             }
             //Handling user input for amount:
             UART_sendString(usertxt);
             UART_getLine(buffer,30);
             UART_sendString("\r\n");
             itemTotal = atoi(buffer);
             if(Result==1)
             {
                 sale += itemTotal*2; //2 dollars per dozen eggs
             }
             else if(Result==2)
             {
                 sale += itemTotal*1;// 1 dollar per pound of chicken. god i wish it was this cheap
             }
             else if(Result==3)
             {
                 sale += itemTotal*2;//2 dollars per gallon of milk
             }


             UART_sendString(marketbot);
             UART_sendString("Do you like to order more? yes/no: ");
             UART_getLine(buffer,30);
             UART_sendString("\r\n");


             if(strcmp(buffer,"no")==0)
             {
                 addItem =0;
                 UART_sendString(marketbot);
                 UART_sendString("The Total sale for all items come to $");
                 snprintf(buffer,30,"%d",sale);
                 UART_sendString(buffer);
                 UART_sendString(". Thank you for shopping with me ");
                 UART_sendString(username);
                 UART_sendString("!\r\n\r\n");
             }
         }
    }
    return 0;
}
