
#include <xc.h>
#include "config.h"
#include "usart.h"

/*
 Configuration the RS232 comunication with 8 bit, 9600 baud rate, in asynchronous mode
 */
void configRS232(){

    //Register TXSTA
                    //CRSC in syncronous mode don´t care
    TX9 = 0;        //8 Bit transmission
    TXEN = 1;       //Transmit enabled
    SYNC = 0;       //Asynchronous mode
    BRGH = 1;       //In asynchronous mode - High Speed

    //Register RCSTA
    SPEN = 1;       //Serial port enable, RX and TX as serial pins
    RX9 = 0;        //8 Bit Reception
    CREN = 1;       //Enables reciever
                    //ADDEN in 8 bit reception don´t care
                    //SREN don´t care in asynchronous mode

    //Others
    BRG16 = 0;
    SPBRG = 129;    //9600 BAUD Rate - See table on datasheet

    RXDTP = 0;      //O que eh isso[interrogacao]
}

void configUSARTInterrupts()
{
    //For EUSART TX interruptions
    TXIE = 0; //Seting the TX interruption enable
    TXIF = 0; //Clean the TX interruption flag

    //For EUSART RX interruptions
    RCIE = 1; //Seting the RC interruption enable
    RCIF = 0; //Clean the RC interruption flag

    PEIE = 1; //Enabling the peripheral interruptions
    GIE = 1; //Enabling the interruptions
}

void putch(unsigned char byte)
{
    while (!TXIF)
        continue;
    TXREG = byte;
}



unsigned char
getch() {
	// recebe um byte
	while(!RCIF)	//nível lógico alto quando o registrador não está vazio
		continue;      
        return RCREG;
}

unsigned char
getche(void)
{
	unsigned char c;
	putch(c = getch());
	return c;
}