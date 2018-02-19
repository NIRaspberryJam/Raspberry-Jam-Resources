import microperi
import scratch

device = microperi.Microbit()
microbit = device.microbit
scr = scratch.Scratch()

while True:
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    z = microbit.accelerometer.get_z()
    a = microbit.button_a.is_pressed()
    b = microbit.button_b.is_pressed()
    
    scr.sensorupdate({'x' : x})
    scr.sensorupdate({'y' : y})
    scr.sensorupdate({'z' : z})
    scr.sensorupdate({'a' : a})
    scr.sensorupdate({'b' : b})

    microbit.sleep(100)
