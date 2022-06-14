sudo rm /etc/apt/preferences.d/nosnap.pref
python3 install-ext.py
sh install-programs.sh
cp .imwheelrc ~
chmod +x open-terminal

mkdir -p ~/.config/autostart
cp imwheel.desktop ~/.config/autostart

sh install-oh-my-zsh.sh
