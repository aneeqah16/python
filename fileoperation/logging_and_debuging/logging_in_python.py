import logging as lg

# Using print statements for logging in production-grade code is not a good practice.
# Instead, we can use the logging module to record events in a file, which is more suitable for production environments.

# Setting the basic configuration for logging
lg.basicConfig(filename="test.log", level=lg.INFO)

# Logging an info message
lg.info("Log this line of execution")
lg.info("This is my print statement.")

# The logging module allows us to save messages that we would typically print on the console to a file permanently.

# Different log levels available in the logging module:
# 1. NOTSET
# 2. DEBUG
# 3. INFO
# 4. WARNING
# 5. ERROR
# 6. CRITICAL

# The log levels determine the severity of the messages to be logged.
# If we set the logging level to INFO, it means we can log messages of INFO level and higher (e.g., WARNING, ERROR, CRITICAL), but we cannot log messages with a lower severity (e.g., DEBUG).

# For example:

lg.warning("This is my warning message.")  # Can be logged as the level is WARNING, which is higher than INFO
lg.error("This is my error message.")  # Can be logged as ERROR is higher than INFO

# The following line will not be logged because the level is set to INFO, and DEBUG messages are lower in severity.
lg.debug("This is my debug message.")  # Cannot be logged as DEBUG is lower than INFO

lg.info("This is my info message.")  # This will be logged because INFO is the set level
lg.critical("This is my critical message.")  # This will be logged because CRITICAL is higher than INFO

# Another info message to show that multiple messages can be logged
lg.info("This is another info message.")

# Shuts down the logging system (flushes any remaining log messages)
lg.shutdown()
