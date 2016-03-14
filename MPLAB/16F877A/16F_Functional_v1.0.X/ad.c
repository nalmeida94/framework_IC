
#include <xc.h>
#include "config.h"
#include "ad.h"

/*
 Config all the 13 channels as analog. With interruption.
 
 */

void configADInterrupt(){
    PIR1bits.ADIF = 0;
    PIE1bits.ADIE = 1;
    
    INTCONbits.GIE = 1;
    INTCONbits.PEIE = 1;
}

void configAD(){
    ADCON0bits.ADON = 1;
    
    
    //right justified
    ADFM = 1;
    
    //A0 - A9 are Analog
    ADCON1bits.PCFG3 = 0;
    ADCON1bits.PCFG2 = 1;
    ADCON1bits.PCFG1 = 0;
    ADCON1bits.PCFG0 = 1;

    /*
    //2 TAD
    ADCON2bits.ACQT2 = 0;
    ADCON2bits.ACQT1 = 0;
    ADCON2bits.ACQT0 = 1;
    */
    
    
    //FOSC/16
    ADCS2 = 0;
    ADCS1 = 1;
    ADCS0 = 0;
    /*
    //FOSC/16
    ADCON2bits.ADCS2 = 1;
    ADCON2bits.ADCS1 = 0;
    ADCON2bits.ADCS0 = 1;
    */

}

void selectChanel(unsigned char channel){
    if(channel == 0){
        ADCON0bits.CHS2 = 0;
        ADCON0bits.CHS1 = 0;
        ADCON0bits.CHS0 = 0;
    }
    else if(channel == 1){
        ADCON0bits.CHS2 = 0;
        ADCON0bits.CHS1 = 0;
        ADCON0bits.CHS0 = 1;
    }
    else if(channel == 2){
        ADCON0bits.CHS2 = 0;
        ADCON0bits.CHS1 = 1;
        ADCON0bits.CHS0 = 0;
    }
    else if(channel == 3){
        ADCON0bits.CHS2 = 0;
        ADCON0bits.CHS1 = 1;
        ADCON0bits.CHS0 = 1;
    }
    else if(channel == 4){
        ADCON0bits.CHS2 = 1;
        ADCON0bits.CHS1 = 0;
        ADCON0bits.CHS0 = 0;
    }
    else if(channel == 5){
        ADCON0bits.CHS2 = 1;
        ADCON0bits.CHS1 = 0;
        ADCON0bits.CHS0 = 1;
    }
    else if(channel == 6){
        ADCON0bits.CHS2 = 1;
        ADCON0bits.CHS1 = 1;
        ADCON0bits.CHS0 = 0;
    }
    else if(channel == 7){
        ADCON0bits.CHS2 = 1;
        ADCON0bits.CHS1 = 1;
        ADCON0bits.CHS0 = 1;
    }
}