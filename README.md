# DAQ

Code for Static Test Stand DAQ

## Teensy Pin Assignemnts

| Teensy Pin |                  Target                   |
| :--------: | :---------------------------------------: |
| 11 (MISO0) |    Thermocouple Boards SO (Serial Out)    |
| 13 (SCK0)  |  Thermocouple Boards SCK (Serial Clock)   |
|     16     |             Thermocouple VCC              |
|     17     |             Thermocouple GND              |
| {35,36,37} | Thermocouple Chip Selects (one per board) |
|     29     |           Load Cell Data ("DT")           |
|     30     |          Load Cell Clock ("SCK")          |
|    A13     |        Pressure Transducer Signal         |

## Load Cell Wiring

| Wire Color | M12 Connector Pin Number | Description  |
| :--------: | :----------------------: | :----------: |
|    Red     |            1             | Excitation + |
|   Black    |            2             | Excitation - |
|   White    |            3             |   Signal -   |
|   Green    |            4             |   Signal +   |

## Resources

[Teensy Pinout](https://www.pjrc.com/teensy/card9a_rev1.pdf)
[Thermocouple Breakout Documentation](https://learn.sparkfun.com/tutorials/max31855k-thermocouple-breakout-hookup-guideZ)
[Load Cell Amp Documentation](https://learn.sparkfun.com/tutorials/load-cell-amplifier-hx711-breakout-hookup-guide/all) *Note: description is for a different breakout board, but uses the same SOC.*
[Load Cell Connector Pinout](https://ptglobal-cdn.s3.ap-southeast-2.amazonaws.com/file_asset_store/fileasset/300/file/39e91befa7.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJEAX2FF3ZMX66G3Q%2F20200131%2Fap-southeast-2%2Fs3%2Faws4_request&X-Amz-Date=20200131T051506Z&X-Amz-Expires=900&X-Amz-SignedHeaders=host&X-Amz-Signature=243de9526c2ff692fd20c8bb86888d24aea5ec9f95a52d6aeea2c118842127e3)