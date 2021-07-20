#Based on I2C Library in i2c_dev of SRL_cFS Repository

from enum import Enum
from os import X_OK, write
import array, fcntl, struct, termios, os
from posixpath import join

I2C_PIPE_DEPTH = 32
MAX_BUS = 64

class i2cSTATE(Enum):
    SUCCESS      = 1
    FAILURE      = 2

def i2c_init():
    print("I2C Initialized.")
    return i2cSTATE.SUCCESS;


#Single Byte I2C Driver


#i2c_open() --> opens the device and returns file

def i2c_open(i2cBUS, addr):

    #Assign Buffer Name
    i2c_buf = "dev/i2c-%d\n" % i2cBUS
    print(i2c_buf)

    #Open i2c Device
    file = open(i2c_buf, "r+")
    
    if(file < 0):
        print("Failed to open i2c Bus: %s", i2c_buf)
        return i2cSTATE.FAILURE

    #Open ioctl op
    if(fcntl.ioctl(file, termios.I2C_SLAVE, addr) < 0):
        print("I2C slave address failed: %d", addr)
        return i2cSTATE.FAILURE

    return file

#i2c_close() --> Closes the open i2c file
def i2c_close(file):
    file.close()

#i2c_write() --> Assumes a one-byte register

#Notes: Will need to add another if statement for when there is no register specified (only one register)
def i2c_write(file, reg, val):
    write_buf = [reg, val]

    if(file.write(write_buf, 2) != 2):
        print("Failed to write register: %x\n", reg)
        return i2cSTATE.FAILURE

    return i2cSTATE.SUCCESS

#i2c_write() --> reads the register

#Notes: Will also need option for if there's only one register
def i2c_read(file, reg, byte_count, buffer):

    if buffer:
        #write to register
        if(i2c_write(file, reg, 1)):

            #read specific number of bytes
            if(file.read(byte_count) != byte_count):
                print("Failed to read from register: %d", reg)
                return i2cSTATE.FAILURE
            else:
                return i2cSTATE.SUCCESS

        else:
            print("Failed to write to register for reading: %d", reg)
            return i2cSTATE.FAILURE

    else:
        print("No existing buffer")
        return i2cSTATE.FAILURE