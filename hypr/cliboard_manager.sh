#!/bin/bash

selection=$(cliphist list | wofi --dmenu)
[ -z "$selection" ] && exit

content=$(cliphist decode "$selection")
echo -n "$content" | wl-copy
notify-send "Clipboard" "Content copied to clipboard" -t 2000