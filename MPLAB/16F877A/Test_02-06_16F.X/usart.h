
#include <xc.h>
#ifndef USART_H
#define	USART_H



#endif	/* USART_H */

void configRS232();
void configUSARTInterrupts();
void putch(unsigned char byte);
unsigned char getch(void);
unsigned char getche(void);