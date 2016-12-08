# Explorer HAT cheatsheet   
### Touch pads

### Inputs   
- `read()` - Read the state of the input
- `has_changed()` - Returns true if the input has changed since the last read
- `on_changed( handler_function[, bounce_time ] )` - Calls "handler_function" when the input changes, debounce time ( in ms ) is optional‰
- `on_low( handler_function[, bounce_time ] )` - Calls "handler_function" when the input goes low ( off )
- `on_high( handler_function[, bounce_time ] )` - Calls "handler_function" when the input goes on ( high )
- `clear_events()` - Remove all handlers   

### Analog Inputs   
The Explorer HAT includes 4 analog sensor inputs. You can use these to read analog voltages for sensors that don't just provide an on or an off input.   
- `eh.analog.one.read()` - Returns the analog voltage (between 0 and 5) from the analog pin. Multiply by 20 to get as a percentage.   
- `eh.analog.one.change( handler_function_name, sensitivity )`    - Sets up a handler function to trigger when the analog value changes by the provided sensitivity.    
### Outputs   
The Explorer HAT includes 4 output pins. These output pins are a little different from the output pins on the Raspberry Pi as they are **current sinks** instead of current sources. This means they act as ground (GND) instead of power (VCC).   
- `on()` - Turns the output on
- `off()` - Turns the output off
- `toggle()` - Changes the output to its opposite state
- `write( boolean )` - Writing 1 or True turns the output on, writing 0 or False turns it off
- `blink( on_time, off_time )` - Turns the output on for "on_time" and then off for "off_time"
- `pulse( fade_in_time, fade_out_time, on_time, off_time )` - Same as blink, but lets you fade between on and off
- `fade( from, to, time )` - Fade from 0-100 to 0-100 brightness over a number of seconds specified by "time"
- `stop()` - Stops any running blink, fade or pulse action
- `brightness(percentage)` - Sets output brightness as a percentage.   
### Light

There are four lights on Explorer HAT, Yellow, Blue, Red and Green. They work just like normal outputs.

```python
explorerhat.light.yellow
...
explorerhat.light.green
```

### Motor

- `invert()` - Reverses the direction of forwards for this motor
- `forwards( speed )` - Turns the motor "forwards" at speed ( default 100% )
- `backwards( speed )` - Turns the motor "backwards" at speed ( default 100% )
- `speed(-100 to 100)` - Moves the motor at speed, from full backwards to full forwards
