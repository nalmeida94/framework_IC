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

unsigned char id = 28;
unsigned char dia = 0;
unsigned char mes = 0;
unsigned char ano = 0;
unsigned char hora = 0;
unsigned char minuto = 0;
unsigned char segundo = 0;


#define MAX 25
#define led1 PORTDbits.RD3

unsigned char string[MAX+1];
unsigned char string_aux[MAX+1];
unsigned  char i = 0;

unsigned short int data_ADC = 0;

unsigned char channel = 1;

char contLedRD4 = 0;
bit changing = 0;
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
        //ADCON0bits.GO_DONE = 1;
        PIR1bits.ADIF = 0;
    }
    //TIMER0
    if(INTCONbits.TMR0IF){
        contLedRD4++;       
        changing = ~changing;        
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
     
    //I2C_Write_Byte(0x00); // Inicializa com 00 segundos.
    I2C_Write_Byte(0x00);
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    //I2C_Write_Byte(0x08); // Inicializa com 8 minutos.
    I2C_Write_Byte(0x30);
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    //I2C_Write_Byte(0x08); // Inicializa com 08:00hs (formato 24 horas).
    I2C_Write_Byte(0x14); //19 horas
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    //I2C_Write_Byte(0x04); // Inicializa com terça
    I2C_Write_Byte(0x04);
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    //I2C_Write_Byte(0x17); // Inicializa com dia 17
    I2C_Write_Byte(0x22);// dia 20 do mês
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    //I2C_Write_Byte(0x04); // Inicializa com mês 04
    I2C_Write_Byte(0x01); //mês 1, janeiro
    I2C_Idle(); //Verifica e aguarda até o barramento I2C estar disponível.
    //I2C_Write_Byte(0x13); // Inicializa com ano 13
    I2C_Write_Byte(0x16); //ano 16
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
    TRISDbits.TRISD3 = 0;
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
    selectChanel(channel);
    
    
    write_RTC_I2c();
    while (1){

        if(contLedRD4 == TIMER0_INTERRUPTS_PER_SECOND*2){
            ADCON0bits.GO_DONE = 1;
            //Leitura de Posição de data no DS-1307.
            read_RTC_I2c(0x04);
            dia = leitura;            
            __delay_ms(10);
            
            //Leitura de Posição de mês no DS-1307.
            read_RTC_I2c(0x05);
            mes = leitura;            
            __delay_ms(10);
            
            //Leitura de Posição de ano no DS-1307.
            read_RTC_I2c(0x06);
            ano = leitura;            
            __delay_ms(10);
            
            //Leitura de Posição da Hora no DS-1307.
            read_RTC_I2c(0x02);
            hora = leitura;            
            __delay_ms(10);

            //Leitura de Posição de Minuto no DS-1307.
            read_RTC_I2c(0x01);
            minuto = leitura;
            __delay_ms(10);

            //Leitura de Posição de Segundo no DS-1307.
            read_RTC_I2c(0x00);
            segundo = leitura;
            
            
            //"id&valor&ano-mes-dia hora:minuto:segundo"
            printf("%u&%u&20%02X-%02X-%02X %02X:%02X:%02X", id, data_ADC, ano, mes, dia, hora, minuto, segundo);

            __delay_ms(10);
            //TODO tirar daqui
            printf("\n");
            led1 = changing;
            contLedRD4 = 0;
        }
    }
}