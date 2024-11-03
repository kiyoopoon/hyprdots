#!/bin/bash
sleep 4
# Kill any existing ags instances
# killall ags

# Start AGS
ags &

# Log AGS output
ags 2>&1 | tee /tmp/ags.log
