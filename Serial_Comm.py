# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:35:56 2022

@author: harpreet.singh
"""

import serial
import struct
import os
import sys
import glob


#BL Commands
COMMAND_BL_GET_VER                                  =0x51
COMMAND_BL_GET_HELP                                 =0x52
COMMAND_BL_GET_CID                                  =0x53
COMMAND_BL_GET_RDP_STATUS                           =0x54
COMMAND_BL_GO_TO_ADDR                               =0x55
COMMAND_BL_FLASH_ERASE                              =0x56
COMMAND_BL_MEM_WRITE                                =0x57
COMMAND_BL_EN_R_W_PROTECT                           =0x58
COMMAND_BL_MEM_READ                                 =0x59
COMMAND_BL_READ_SECTOR_P_STATUS                     =0x5A
COMMAND_BL_OTP_READ                                 =0x5B
COMMAND_BL_DIS_R_W_PROTECT                          =0x5C
COMMAND_BL_MY_NEW_COMMAND                           =0x5D


#len details of the command
COMMAND_BL_GET_VER_LEN                              =6
COMMAND_BL_GET_HELP_LEN                             =6
COMMAND_BL_GET_TORQUE_LEN_LEN                       =6
COMMAND_BL_GET_RPM_LEN_LEN                          =6
COMMAND_BL_GO_FORCE_LEN                             =6
COMMAND_BL_MY_NEW_COMMAND_LEN                       =6


verbose_mode = 1
mem_write_active =0

#----------------------------- utilities----------------------------------------

def word_to_byte(addr, index , lowerfirst):
    value = (addr >> ( 8 * ( index -1)) & 0x000000FF )
    return value

def get_crc(buff, length):
    Crc = 0xFFFFFFFF
    #print(length)
    for data in buff[0:length]:
        Crc = Crc ^ data
        for i in range(32):
            if(Crc & 0x80000000):
                Crc = (Crc << 1) ^ 0x04C11DB7
            else:
                Crc = (Crc << 1)
    return Crc


#----------------------------- Serial Port ----------------------------------------
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def Serial_Port_Configuration(port):
    global ser
    try:
        ser = serial.Serial(port,115200,timeout=2)
    except:
        print("\n   Oops! That was not a valid port")
        
        port = serial_ports()
        if(not port):
            print("\n   No ports Detected")
        else:
            print("\n   Here are some available ports on your PC. Try Again!")
            print("\n   ",port)
        return -1
    if ser.is_open:
        print("\n   Port Open Success")
    else:
        print("\n   Port Open Failed")
    return 0

              
def read_serial_port(length):
    read_value = ser.read(length)
    return read_value

def Close_serial_port():
    pass
def purge_serial_port():
    ser.reset_input_buffer()
    
def Write_to_serial_port(value, *length):
        data = struct.pack('>B', value)
        if (verbose_mode):
            value = bytearray(data)
            #print("   "+hex(value[0]), end='')
            print("   "+"0x{:02x}".format(value[0]),end=' ')
        if(mem_write_active and (not verbose_mode)):
                print("#",end=' ')
        ser.write(data)

#----------------------------- command processing----------------------------------------

def process_COMMAND_BL_MY_NEW_COMMAND(length):
    pass

def process_COMMAND_BL_GET_VER(length):
    ver=read_serial_port(1)
    value = bytearray(ver)
    print("\n   Bootloader Ver. : ",hex(value[0]))

def process_COMMAND_BL_GET_HELP(length):
    #print("reading:", length)
    value = read_serial_port(length) 
    reply = bytearray(value)
    print("\n   Supported Commands :",end=' ')
    for x in reply:
        print(hex(x),end=' ')
    print()

#------------------------------COmmand decode-------------------------------------------------

def decode_menu_command_code(command):
    ret_value = 0
    data_buf = []
    for i in range(255):
        data_buf.append(0)
    
    if(command  == 0 ):
        print("\n   Exiting...!")
        raise SystemExit
    elif(command == 1):
        print("\n   Command == > BL_GET_VER")
        COMMAND_BL_GET_VER_LEN              = 6
        data_buf[0] = COMMAND_BL_GET_VER_LEN-1 
        data_buf[1] = COMMAND_BL_GET_VER 
        crc32       = get_crc(data_buf,COMMAND_BL_GET_VER_LEN-4)
        crc32 = crc32 & 0xffffffff
        data_buf[2] = word_to_byte(crc32,1,1) 
        data_buf[3] = word_to_byte(crc32,2,1) 
        data_buf[4] = word_to_byte(crc32,3,1) 
        data_buf[5] = word_to_byte(crc32,4,1) 

        
        Write_to_serial_port(data_buf[0],1)
        for i in data_buf[1:COMMAND_BL_GET_VER_LEN]:
            Write_to_serial_port(i,COMMAND_BL_GET_VER_LEN-1)
        

        ret_value = read_bootloader_reply(data_buf[1])


#----------------------------- Ask Menu implementation----------------------------------------


name = input("Enter the Port Name of your device(Ex: COM3):")
ret = 0
ret=Serial_Port_Configuration(name)
if(ret < 0):
    decode_menu_command_code(0)
    

    
  
while True:
    print("\n +==========================================+")
    print(" |                  Menu                      |")
    print(" |         STM32F4 Command Center v1        |")
    print(" +==========================================+")

  
    
    print("\n   Which BL command do you want to send ??\n")
    print("   BL_GET_VER                            --> 1")
    print("   BL_GET_HLP                            --> 2")
    print("   BL_GET_TORUQE                         --> 3")
    print("   BL_GET_RPM                            --> 4")
    print("   BL_GO_FORCE                           --> 5")
    print("   MENU_EXIT                             --> 0")

    #command_code = int(input("\n   Type the command code here :") )

    command_code = input("\n   Type the command code here :")

    if(not command_code.isdigit()):
        print("\n   Please Input valid code shown above")
    else:
        decode_menu_command_code(int(command_code))

    input("\n   Press any key to continue  :")
    purge_serial_port()





    

def check_flash_status():
    pass

def protection_type():
    pass
