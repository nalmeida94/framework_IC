#include <xc.h>
#include <stdio.h>
#include <string.h>

#include "config.h"
#include "constants.h"

#include "i2c.h"
#include "usart.h"
#include "ad.h"
#include "timer0.h"

bit hasAnError = 0;
unsigned char receivedData = 'X';
unsigned char leitura = 0;

#define MAX 25
#define led1 PORTDbits.RD3
#define led2 PORTDbits.RD4

unsigned char string[MAX+1];
unsigned char string_aux[MAX+1];
unsigned  char i = 0;

unsigned int data_ADC = 0;



bit val = 0;

void interrupt interruptions(void){
    //USART
    if (RCIF){
        if (FERR || OERR) //checking for framing and overrun erros
        {
            CREN = 0; //if an error occur, clear the error desabling the reciever
            hasAnError = 1;
            CREN = 1;
        }

        receivedData = RCREG;

        if(receivedData == '\r')
        {
                string_aux[i] = '\0';
                strcpy(string,string_aux);
                printf("\n\r");
                i = 0;
        }else
        {
                if(i < MAX)
                {
                        i = i%MAX;
                        string_aux[i] = receivedData;
                        i++;
                }
                if(i == MAX)
                        i++;
        }
    }
    //AD
    if(PIR1bits.ADIF){
        data_ADC = ((ADRESH<<8) + ADRESL);
        ADCON0bits.GODONE = 1;
        PIR1bits.ADIF = 0;
    }
    //TIMER0
    if(INTCONbits.TMR0IF){
        val = ~val;
        led2 = val;
        //PORTBbits.RB0 = val;
        INTCONbits.TMR0IF = 0;        
    }    
}

void write_RTC_I2c()
{
    I2C_Idle();
    I2C_Start(); // Inicializa a comunicação I2c
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    I2C_Write_Byte(0xD0); // End. fixo para DS1307: 1101000X, onde x = 0 é para gravação.
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    I2C_Write_Byte(0x00); // End. onde começa a programação do relógio, end. dos segundos.
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    I2C_Write_Byte(0x00); // Inicializa com 00 segundos.
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    I2C_Write_Byte(0x08); // Inicializa com 8 minutos.
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    I2C_Write_Byte(0x08); // Inicializa com 08:00hs (formato 24 horas).
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    I2C_Write_Byte(0x04); // Inicializa com terça
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    I2C_Write_Byte(0x17); // Inicializa com dia 17
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    I2C_Write_Byte(0x04); // Inicializa com mês 04
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    I2C_Write_Byte(0x13); // Inicializa com ano 13
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    I2C_Stop(); // Finaliza a comunicação I2c
}

void read_RTC_I2c(unsigned char pos_memoria)
{
    I2C_Idle();
    I2C_Start();
    I2C_Idle();
    I2C_Write_Byte(0xD0); //address of DS1307.
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    I2C_Write_Byte(pos_memoria); // Position the address pointer to 0.
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    I2C_ReStart();
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    I2C_Write_Byte(0xD1); // Direction bit set to read.
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    leitura = I2C_Read_Byte();
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    I2C_Send_NACK();
    I2C_Stop();
}

void main(void){
    TRISD3 = 0;
    TRISD4 = 0;
    //timer
    configTimer();
    
    //ad
    configADInterrupt();
    configAD();
    
    //usart
    configRS232();
    configUSARTInterrupts();
    
            
    //I2C
    InitI2C_Master();
    
    //interrupts
    unsigned char channel = 1;
    selectChanel(channel);
    ADCON0bits.GODONE = 1;


    printf("\n\n\rwrite_RTC_I2c()\n\n");

    for(int i=0; i<(2000/20); i++)
    {
        __delay_ms(20);
    }
    write_RTC_I2c();

    printf("\n\n\rLet The Carnage Begin, now!\n\n");

    while (1){
        for(int i=0; i<(2000/20); i++)
        {
            __delay_ms(20);
        }

        //Leitura de Posição da Hora no DS-1307.
        read_RTC_I2c(0x02);
        printf("\n\rLeitura Hora: [ %02X ]", leitura);

        __delay_ms(10);

        //Leitura de Posição de Minuto no DS-1307.
        read_RTC_I2c(0x01);
        printf("\n\rLeitura Minuto: [ %02X ]", leitura);

        __delay_ms(10);

        //Leitura de Posição de Segundo no DS-1307.
        read_RTC_I2c(0x00);
        printf("\n\rLeitura Segundo: [ %02X ]", leitura);

        __delay_ms(10);
        
        printf("\n\rRegistrou %u", data_ADC);

        __delay_ms(10);
        
        printf("\n\r\n\r\n\r");
    }
}