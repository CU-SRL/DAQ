# Control Computer/DAQ

## Objects/Classes

![Class Diagram](images/class_diagram.svg)

### Rocket Side

#### `RocketSideListen`

- Socket server listening for commands via UDP
- Producer for command message queue

#### `RockerSideTalk`

- Talk socket sending telemetry via UDP
- Consumer of telemetry queue

#### `SensorRead`

- Handles all sensor I/O interactions
- Producer for sensor data queue
- Producer for telemetry queue (downlink raw sensor data)

#### `ControlWrite`

- Handles all servo control interactions
- Receives commands from Hypervisor
- Unnecessary? Could the hypervisor handle all control?
- What does communication look like from the hypervisor to here? Pipe?

#### `Hypervisor`

- Implement onboard control law
- Synthesize sensor data and commands into control outputs
- Producer for telemetry queue (downlink information about spacecraft state, servo positions, etc.)
- Consumer for command queue
- Consumer for sensor data queue
- Send data to `ControlWrite`

---

## Hardware

![Hardware Diagram](images/hardware_diagram.svg)