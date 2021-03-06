from enum import IntEnum


class Device():
    def __init__(self):
        return


"""Enum differentiates between input and output devices
"""


class IOClass(IntEnum):
    INPUT = 1
    OUTPUT = 2


"""Enumerate available hardware busses
"""


class IOBus(IntEnum):
    I2C = 1
    SPI = 2


"""Encapsulate information about a single thermocouple
"""


class KThermocouple():
    """Constructor
    
    @param name: string identifier of this interface
    @param channel: channel of this interface on the ADC
    @param purpose: string descriptor
    @param displayed: boolean true/false for UI
    """
    def __init__(self, name, channel, purpose, displayed):
        self.name = name
        self.channel = channel
        self.purpose = purpose
        self.displayed = displayed
        return


class PressureTransducer():
    """Constructor
    
    @param name: string identifier of this interface
    @param channel: channel of this interface on the ADC
    @param purpose: string descriptor
    @param pressureRange: maximum pressure value, in PSI
    @param scale: voltage to PSI scaling factor
    @param displayed: boolean true/false for UI
    """
    def __init__(self, name, channel, purpose, pressureRange, scale, displayed):
        self.name = name
        self.channel = channel
        self.purpose = purpose
        self.pressureRange = pressureRange
        self.scale = scale
        self.displayed = displayed
        return


"""ADS1115 ADC Hardware class
"""


class ADS1115Thermo(Device):
    ioclass = IOClass.INPUT

    """Constructor
    
    @param address: I2C address of the device
    @param thermocouples: list of KThermocouple instances
    """

    def __init__(self, address, thermocouples):
        self.address = address
        self.thermocouples = thermocouples
        return


class HX711(Device):
    ioclass = IOClass.INPUT
    iobus = IOBus.I2C
    """Constructor
    
    @param address: I2C address of the device
    @param scale: force scaling factor for load cell
    """
    def __init__(self, address, scale):
        self.address = address
        self.scale = scale
        return
