import logging as lg

# Setting the basic configuration for logging
# We specify the log file name ("test1.log"), the logging level (DEBUG), and the format for log messages.
# The format includes both the timestamp and the actual message. 
# %(asctime)s will include the timestamp, and %(message)s will include the log message.
lg.basicConfig(filename="test1.log", level=lg.DEBUG, format='%(asctime)s,%(message)s')

# Logging messages at different levels
# This line logs an info message. Since the logging level is set to DEBUG, it will be recorded in the log.
lg.info("This is my info message")

# Logging an error message. As with the info message, this will be recorded because ERROR is a higher level than INFO.
lg.error("This is error logging")

# Logging a critical message. Critical messages are the highest severity level and will also be logged.
lg.critical("This is my critical message")

# Shutting down the logging system to ensure all messages are written to the log file
lg.shutdown()
