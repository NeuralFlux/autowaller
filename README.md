# autowaller
Scrap popular QuoteFancy wallpapers and change them at a defined frequency.

## Getting Started (Linux based systems)
**Important - I've tried it on Ubuntu with Gnome Desktop. It will presumably be different for other distro/OS. A minor fix in the `change_wallpaper` function should be able to do it.**
1. Clone the repo - `git clone https://github.com/NeuralFlux/autowaller`
2. `cd autowaller`
3. `pip3 install -r requirements.txt`
4. Open `Startup Applications`
5. Add the command `python3 $PATH_TO_CLONE_DIR/autowaller.py --freq $NUM` where `$NUM` specifies how frequently this program runs (in seconds, `default=3600`)
6. Fill the remaining details

It should look like this
<center><img src="https://i.postimg.cc/PfDS47TL/Screenshot-from-2021-03-23-19-03-40.png"/></center>

7. Press `Save` and Reboot your PC
