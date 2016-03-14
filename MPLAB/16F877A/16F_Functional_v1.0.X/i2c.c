/*
 * File:   i2c.c
 * Author: Nathan
 *
 * Created on 14 de Março de 2016, 08:46
 */


#include <xc.h>
#include "i2c.h"

void InitI2C_Master(void)
{
    SDA_DIR = 1;
    SCL_DIR = 1;

    SSPADD = ( _XTAL_FREQ / (4*I2C_SPEED) ) - 1;
    //SSPADD = 49;      //I2C Clock at 100KHz
    
    SSPIF = 0;
    
    //SSPSTAT = 0x80;
     SSPSTAT = 0;
     SSPSTATbits.SMP = 1;   //Slew rate control disabled for Standard Speed mode (100 kHz and 1 MHz)
     SSPSTATbits.CKE = 0;   //Disable SMBus specific inputs

    //SSPCON = 0x28;
    //SSPCON1 = 0x00;
    WCOL = 0;
    SSPOV = 0;
    SSPEN = 0;
    CKP = 0;
    
     SSPM3 = 0;
     SSPM2 = 1;
     SSPM1 = 1;
     SSPM0 = 0;
     //SSPM = 0b0110;
     SSPEN = 1;         //Enables the serial port
}


void InitI2C_Slave(char address)
{
    SDA_DIR = 1;
    SCL_DIR = 1;

    SSPCON2bits.GCEN = 1;       //Enable interrupt when a general call address (0000h)

    SSPADD = address;
    SSPIF = 0;

    //SSPSTAT = 0x80;
     SSPSTAT = 0;
     SSPSTATbits.SMP = 1;   //Slew rate control disabled for Standard Speed mode (100 kHz and 1 MHz)
     SSPSTATbits.CKE = 0;   //Disable SMBus specific inputs

    //SSPCON = 0x36;
    //SSPCON1 = 0x00;
    WCOL = 0;
    SSPOV = 0;
    SSPEN = 0;
    CKP = 0;
    
     SSPM3 = 0;
     SSPM2 = 1;
     SSPM1 = 1;
     SSPM0 = 0;
     //SSPM = 0b0110;     //SSPM3:SSPM0 - I2C Slave mode, 7-bit address
     CKP = 1;           //Release clock
     SSPEN = 1;         //Enables the serial port
}

void I2C_Start(void)
{
    SSPCON2bits.SEN = 1; // initiate bus start condition
    while (!SSPIF); // wait the start condition
    SSPIF = 0;
}

void I2C_ReStart(void)
{
    SSPCON2bits.RSEN = 1;
    while (!SSPIF);
    SSPIF = 0;
}

void I2C_Stop(void) {
    SSPCON2bits.PEN = 1;
    while (!SSPIF);
    SSPIF = 0;
}

void I2C_Send_ACK(void) {
    SSPCON2bits.ACKDT = 0;
    SSPCON2bits.ACKEN = 1;
    while (!SSPIF);
    SSPIF = 0;
}

void I2C_Send_NACK(void) {
    SSPCON2bits.ACKDT = 1;
    SSPCON2bits.ACKEN = 1;
    while (!SSPIF);
    SSPIF = 0;
}

bit I2C_Write_Byte(unsigned char Byte) {
//BOOL I2C_Write_Byte(unsigned char Byte) {
    SSPBUF = Byte;
    while (!SSPIF);
    SSPIF = 0;
    return SSPCON2bits.ACKSTAT;
}

unsigned char I2C_Read_Byte(void)
{
    SSPCON2bits.RCEN = 1;
    while (!SSPIF);
    SSPIF = 0;

    return SSPBUF;
}

void I2C_Idle( void )
{
  while ( ( SSPCON2 & 0x1F ) || ( SSPSTATbits.R_W ) )
     continue;
}
