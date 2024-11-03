# ~/.config/fish/config.fish

# Alias for neofetch
alias sf="~/.config/neofetch/simple.sh"
alias ff="~/codes/fetch.sh"

if status is-interactive
    # Commands to run in interactive sessions can go here
end

# Remove fish greeting
set fish_greeting ""

# Run neofetch
# sf

function get_hour
    date +%H
end

function anime_waifu_greetings
    set hour (get_hour)
    if test $hour -ge 5 -a $hour -lt 12
        echo "Good morning darling~ Make sure to take breakfast, hun~"
    else if test $hour -ge 12 -a $hour -lt 15
        echo "Good noon~ Enjoy your lunch, darling~"
    else if test $hour -ge 15 -a $hour -lt 18
        echo "Good afternoon, sweetie~ Hope you're having a great day~"
    else if test $hour -ge 18 -a $hour -lt 21
        echo "Good evening, darling~ Don't forget to relax~"
    else if test $hour -ge 21 -a $hour -lt 23
        echo "It's night time, hun~ Make sure to get some rest~"
    else
        echo "Eh?! Why are you still awake, hun? Go to sleep now~"
    end
end

neofetch
# anime_waifu_greetings | lolcat
python3 ~/codes/waifu_greeting.py
# echo " "

# Initialize starship
# starship init fish | source

# Key bindings
bind \e\[3\;5~ kill-word  # Ctrl+Delete to delete the next word
bind \cH backward-kill-word  # Ctrl+Backspace to delete the previous word
bind \cU backward-kill-line  # Ctrl+U to delete the whole line
zoxide init fish --cmd cd | source

fish_add_path /home/kiyo/.spicetify
