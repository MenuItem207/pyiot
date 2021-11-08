import spidev
from time import sleep

# create SPI object
spi = spidev.SpiDev()
spi.open(0, 0) # open SPI port 0, device (CS) 0

def read_ADC(ch): # read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
    if (ch > 7) or (ch < 0): # invalid ch num
        return -1
    spi.max_speed_hz = 1350000 # 3.5 MHz
    r = spi.xfer2([1, (8 + ch) << 4, 0]) # send 3 bytes, bits 12-15 are channel num
    return ((r[1] & 3) << 8) + r[2] # return 10 bits

while(True):
    # run forever lol
    val = read_ADC(0) # read from adc channel 0
    print(val)
    sleep(1)