# DAQ Scripting

Scripts can be defined and executed as a series of timed commands. 

The available commands are defined in `command_database.json`.

Scripts are formatted as JSON. One `scripts.json` file may be loaded at a time.

 Within the main object of `scripts.json`, each script is identified by its key. Each script is a list of objects, each corresponding to the execution of one command. The syntax for a command object is as follows:

 ```JSON
{
    "time": <Time from start in seconds>,
    "command_id": <ID of command to execute>,
    "arguments": [
        "list of arguments",
        "for the given command"
    ]
}
 ```
 
 
The provided example `scripts_example.json` demonstrates a script which sets all servos to fully open, then closes them sequentially, separated by one second.

Note that the execution rate of script commands is limited by the loop rate of the `Hypervisor` thread. If multiple sequential, tightly-timed commands are needed, use a high loop rate.
