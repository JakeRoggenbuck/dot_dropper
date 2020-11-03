import subprocess
import inquirer
import yaml


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
        subprocess.run([f"diff -u --color {self.in_git} {self.in_use}"], shell=True)

    def copy_file(self):
        subprocess.run([f"/bin/cp -f {self.in_use} {self.in_git}"], shell=True)

    def has_diff(self):
        return False if self.get_diff() == [0, 0] else True


class Config:
    def __init__(self, path: str):
        self.path = path
        self.config = self.get_config()

    def get_config(self):
        config_file = open(self.path)
        config = yaml.load(config_file, Loader=yaml.FullLoader)
        return config


if __name__ == "__main__":
    config_file = Config("/home/jake/Repos/dot_drop/config.yml").config
    for config in config_file["configs"]:
        copy = CopyDot(config["in_use"], config["in_git"])
        if copy.has_diff():
            copy.show_diff()
            copy.copy_file()
