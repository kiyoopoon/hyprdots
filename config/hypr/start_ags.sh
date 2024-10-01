#!/bin/bash
killall ags

sleep 1
ags &

# Log AGS output
ags 2>&1 | tee /tmp/ags.log
