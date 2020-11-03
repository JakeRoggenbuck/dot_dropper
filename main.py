import subprocess
import inquirer


class CopyDot:
    def __init__(self, in_use: str, in_git: str):
        self.in_use = in_use
        self.in_git = in_git

    def get_diff(self):
        check_nums = []
        for check in ["^<", "^>"]:
            check_num = subprocess.check_output(
                [f'diff {self.in_git} {self.in_use} | grep "{check}" | wc -l'], shell=True)
            check_nums.append(int(check_num.decode("utf-8").strip("\n")))
        return check_nums

    def show_diff(self):
        subprocess.run([f"diff -u {self.in_git} {self.in_use} | less"], shell=True)

    def copy_file(self):
        subprocess.run([f"/bin/cp -f {self.in_use} {self.in_git}"], shell=True)

    def has_diff(self):
        return False if self.get_diff() == [0, 0] else True



a = "/home/jake/.config/bspwm/bspwmrc"
b = "/home/jake/Repos/dotfiles/bspwm/bspwmrc"

copy = CopyDot(a, b)
if copy.has_diff():
    copy.show_diff()
    copy.copy_file()

"""

    def ask_for_files(self, files: list):
        questions = [
            inquirer.Checkbox(
                "diff",
                message="View diff ",
                choices=files,
            ),
        ]
        answers = inquirer.prompt(questions)
        return answers

"""
