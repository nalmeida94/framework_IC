/*
 * File:   timer0.c
 * Author: Nathan
 *
 * Created on 14 de Março de 2016, 08:47
 */


#include <xc.h>
#include "config.h"
#include "timer0.h"

/*
 * Configuring the timer to 8 bits counter with 256 presacaler with interruption.
 * ((20.000.000 Hz /4 cicles of the processor)/256 counter)/256 of the preescaler = 76 Hz
 * 76 interrupts by second
 */

void configTimer(){
    OPTION_REGbits.T0CS = 0;//clock interno
    OPTION_REGbits.T0SE = 0;
    OPTION_REGbits.PSA = 0;//timer 0 com pre scaler


    //pre scaler 1:256
    OPTION_REGbits.PS2 = 1;
    OPTION_REGbits.PS1 = 1;
    OPTION_REGbits.PS0 = 1;

    INTCONbits.TMR0IF = 0;//flag
    INTCONbits.TMR0IE = 1;//enable
    INTCONbits.GIE = 1;
    INTCONbits.PEIE = 1;    
}


