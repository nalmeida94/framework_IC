
#include <xc.h>
#ifndef I2C_BYJESUS_H
#define	I2C_BYJESUS_H

#ifdef	__cplusplus
extern "C" {
#endif


#ifdef	__cplusplus
}
#endif

#endif	/* I2C_BYJESUS_H */

#ifndef _XTAL_FREQ
    #define _XTAL_FREQ   20000000
#endif

// Definicao dos pinos para i2c (mssp)
#define SDA		RC4	// Pino de dados para i2c
#define SCL		RC3	// Pino de Clock para i2c
#define SDA_DIR		RC4	// Pino direcao de dados I/O
#define SCL_DIR		RC3	// Pino direcao do Clock I/O

// Velocidade de transmissao i2c
#define I2C_SPEED	100000				// kbps

void InitI2C_Master(void);
void InitI2C_Slave(char address);
void I2C_Start(void);
void I2C_ReStart(void);
void I2C_Stop(void);
void I2C_Send_ACK(void);
void I2C_Send_NACK(void);
bit I2C_Write_Byte(unsigned char);
//BOOL I2C_Write_Byte(unsigned char);
unsigned char I2C_Read_Byte(void);
void I2C_Idle(void);