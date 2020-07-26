import subprocess


dots = [
    ("~/.bashrc", "~/Repos/ConfigFiles/.bashrc"),
    ("~/.config/sxhkd/sxhkdrc", "~/Repos/ConfigFiles/sxhkd/sxhkdrc"),
    ("~/.config/bspwm/bspwmrc", "~/Repos/ConfigFiles/bspwm/bspwmrc"),
    ("~/.config/alacritty/alacritty.yml", "~/Repos/ConfigFiles/alacritty/alacritty.yml"),
    ("~/.config/nvim/init.vim", "~/Repos/ConfigFiles/nvim/init.vim"),
    ("~/.config/polybar/config", "~/Repos/ConfigFiles/polybar/config")
]

for (a, b) in dots:
    diff = input(f"View diff of {a}: ") 
    if diff.upper() == "Y":
        subprocess.run([f"diff -u {b} {a} | less"], shell=True)
    cp = input(f"Copy {a} to {b}: ") 
    if cp.upper() == "Y":
        cped = subprocess.run([f"cp {a} {b}"], shell=True)
