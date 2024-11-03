#!/bin/bash

# Launch CopyQ
copyq menu &

# Wait for CopyQ to start
sleep 2

# Get the window ID of the newly opened CopyQ
WIN_ID=$(hyprctl clients | grep "CopyQ" | awk '{print $1}')

# Print window ID for debugging
echo "Window ID: $WIN_ID"

# Check if window ID is valid
if [ -z "$WIN_ID" ]; then
  echo "Error: Could not find CopyQ window."
  exit 1
fi

# Get mouse location
# You may need to replace this with an appropriate Wayland tool or set manually
MOUSE_X=100  # Replace with actual x-coordinate or use a tool
MOUSE_Y=100  # Replace with actual y-coordinate or use a tool

# Print mouse location for debugging
echo "Mouse Location: X=$MOUSE_X, Y=$MOUSE_Y"

# Position CopyQ under the mouse cursor
hyprctl movewindow $WIN_ID $MOUSE_X $MOUSE_Y

# Optional: Add a longer sleep if the menu disappears too quickly
sleep 5
