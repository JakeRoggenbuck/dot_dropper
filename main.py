import subprocess
from termcolor import colored
from pprint import pprint
import inquirer


dots = [
    ("~/.bashrc", "~/Repos/ConfigFiles/.bashrc"),
    ("~/.config/sxhkd/sxhkdrc", "~/Repos/ConfigFiles/sxhkd/sxhkdrc"),
    ("~/.config/bspwm/bspwmrc", "~/Repos/ConfigFiles/bspwm/bspwmrc"),
    ("~/.config/alacritty/alacritty.yml", "~/Repos/ConfigFiles/alacritty/alacritty.yml"),
    ("~/.config/nvim/init.vim", "~/Repos/ConfigFiles/nvim/init.vim"),
    ("~/.config/polybar/config", "~/Repos/ConfigFiles/polybar/config")
]

w = []
for (a, b) in dots:
    c = ["^>", "^<"];f = [];co = ["green", "red"];g = []
    for t in range(2):
        y = subprocess.check_output([f'diff {b} {a} | grep "{c[t]}" | wc -l'], shell=True).decode("utf-8").strip("\n")
        if int(y) > 0:
            f.append(co[t])
            w.append(a)
        else:
            f.append("white")
        g.append(y)
    print(colored("+"+g[0], f[0]), colored("-"+g[1], f[1]), colored(a.split('/')[-1], f[0]))
    p = a.split('\n')[-1]

if len(w) > 0:
    questions = [
        inquirer.Checkbox(
            "diff",
            message="View diff ",
            choices=w,
        ),
    ]
    answers = inquirer.prompt(questions)
    if len(answers["diff"]) > 0:
        diff = []
    print("Update")
    for j in answers["diff"]:
        for h in dots:
            if h[0] == j:
                subprocess.run([f"diff {h[0]} {h[1]} | less"], shell=True)

if len(w) > 0:
    questions = [
        inquirer.Checkbox(
            "copy",
            message="Copy ",
            choices=w,
        ),
    ]
    answers = inquirer.prompt(questions)
    if len(answers["copy"]) > 0:
        copy = []
        print("Update")
        for j in answers["copy"]:
            copy.append(j)
            print(j) 
        update = input("[Y/n]: ") 

        if update.upper() == "Y":
            for k in copy:
                for h in dots:
                    if h[0] == k:
                        subprocess.run([f"/bin/cp -f {h[0]} {h[1]}"], shell=True)
                        print(colored(f"copied {h[0]}", "green"))
        
                        subprocess.run([f"git add {h[1]}"], shell=True)
        z = f"git commit -m \" Change {' '.join(l.split('/')[-1] for l in copy)}\""
        subprocess.run([z], shell=True)
