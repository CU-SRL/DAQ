# DAQ

Code for Static Test Stand DAQ computer.

## v3.0

### Main Changes

- Add a Raspberry Pi to host a web interface
- Add internal power
- Add support for 15V supply, 0-10V signal pressure transducers

### Raspberry Pi Setup

- Hardware: Raspbery Pi Model 3B
- OS: [Ubuntu Server 18.04LTS for ARM 64-bit](https://ubuntu.com/download/raspberry-pi)
- Web server is Flask in Python

## v2.0

### Main iterative changes

Changes to the DAQ from v1.0 to v2.0 are hardware-based:

- Use a larger enclosure that's easier to work in
- Hard-mount components to minimize risk of physical damage
- Use aviation-style connectors for pressure transducer and load cell connection (v1 had issues with repetitive strain failure on pin-header type connectors)

### Parts List

|      Name/Description      |              Part Number              | Price  | Quantity |
| :------------------------: | :-----------------------------------: | :----: | :------: |
|         Controller         |              Teensy 3.6               | $31.52 |    1     |
|          SD card           |         Kingston 8GB SD Card          | $3.99  |    1     |
|    Thermocouple Modules    |          Sparkfun MAX31855K           | $15.95 |    3     |
|   Thermocouple Connector   |          Sparkfun PCC-SMP-K           | $3.95  |    3     |
|       Thermocouples        |      5pcs 3M Type-K Thermocouple      | $13.66 |    1     |
|       Load Cell Amp        |            Sparkfun HX711             | $9.95  |    1     |
|         Breadboard         |          4pcs Breadboard kit          | $9.99  |    1     |
|        Hookup Wire         |     6 color 22AWG Hookup Wire Kit     | $17.70 |    1     |
|      Breadboard wires      |            Jumper Wire Kit            | $11.99 |    1     |
|         USB Cable          |      "Micro USB 2.0 cable, 3ft."      | $4.99  |    1     |
|       USB Extension        |     Tripp-Lite 15m Active USB 2.0     | $33.32 |    1     |
|       DAQ Connectors       | 10-pair 4 Pin Aviation Plug Connector | $10.90 |    1     |
| Load Cell/Transducer Cable |       500ft. 22/4 Stranded wire       | $29.95 |    1     |
|         Enclosure          |       BUD Industries NBF-32016        | $27.92 |    1     |

### USB Connector Pin Assignments

| USB Color | Pin Number |
| :-------: | :--------: |
|    Red    |     1      |
|   White   |     2      |
|   Green   |     3      |
|   Black   |     4      |


## v1.0

### Teensy Pin Assignments

| Teensy Pin |                  Target                   |
| :--------: | :---------------------------------------: |
| 12 (MISO0) |    Thermocouple Boards SO (Serial Out)    |
| 13 (SCK0)  |  Thermocouple Boards SCK (Serial Clock)   |
|     16     |             Thermocouple VCC              |
|     17     |             Thermocouple GND              |
| {35,36,37} | Thermocouple Chip Selects (one per board) |
|     29     |           Load Cell Data ("DT")           |
|     30     |          Load Cell Clock ("SCK")          |
|    A13     |        Pressure Transducer Signal         |

### Load Cell Wiring

|  Wire Color  | Connector Pin Number | Description  |
| :----------: | :------------------: | :----------: |
|     Red      |          1           | Excitation + |
|    Black     |          2           | Excitation - |
|  White/Blue  |          3           |   Signal -   |
| Green/Yellow |          4           |   Signal +   |

### Resources

[Teensy Pinout](https://www.pjrc.com/teensy/card9a_rev1.pdf)
[Thermocouple Breakout Documentation](https://learn.sparkfun.com/tutorials/max31855k-thermocouple-breakout-hookup-guideZ)
[Load Cell Amp Documentation](https://learn.sparkfun.com/tutorials/load-cell-amplifier-hx711-breakout-hookup-guide/all) *Note: description is for a different breakout board, but uses the same SOC.*
[Load Cell Connector Pinout](https://ptglobal-cdn.s3.ap-southeast-2.amazonaws.com/file_asset_store/fileasset/300/file/39e91befa7.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJEAX2FF3ZMX66G3Q%2F20200131%2Fap-southeast-2%2Fs3%2Faws4_request&X-Amz-Date=20200131T051506Z&X-Amz-Expires=900&X-Amz-SignedHeaders=host&X-Amz-Signature=243de9526c2ff692fd20c8bb86888d24aea5ec9f95a52d6aeea2c118842127e3)