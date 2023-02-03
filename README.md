# Picodebug -- a tool for debugging and logging in MicroPython scripts on Raspberry Pico and Raspberry Pico W

Features:

1. Works without REPL

2. Works in main.py

3. Automatic rotation of logs

4. Using 8 log files of 100KB each, than automatically rotate: log1.txt, log2.txt, log3.txt, log4.txt, log5.txt, log6.txt, log7.txt, log8.txt

5. All debug messages are stored, not rewrited

6. Every log message is timestamped

7. Output to log files and to console

7. Just use __picodebug.logPrint("some log message")__ in your code

8. Using, output to log file

__import picodebug__

__picodebug.logPrint("some log message")__


9. Using, output to log file and console

__import picodebug__

__picodebug.logPrint("some log message", True)__


10. Using, output to console only

__import picodebug__

__picodebug.logPrint("some log message", True, False)__
