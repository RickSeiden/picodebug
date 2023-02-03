import time
import machine

import picodebug


picodebug.logPrint("file begin =======")

sensor_temp = machine.ADC(4)
picodebug.logPrint("sensor defined")
 
picodebug.logPrint("before rtc = machine.RTC()")
rtc = machine.RTC()
picodebug.logPrint("after rtc = machine.RTC()")

picodebug.logPrint("file end =======")
