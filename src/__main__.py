#!/usr/bin/env python3
"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

import sys
from podrum.Server import Server

def usage():
    print("Usage: \"python3 -O src/__main__.py [OPTIONS]\"\nAvaiable Options:\n  --no_wizard  Starts the Server without the Wizard")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "--no_wizard":
                Server(False)
        else:
            usage()
    else:
        Server(True)
