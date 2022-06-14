import os
from typing import List

BEGIN_STR = "# configurator begin"
END_STR = "# configurator end"

def dirOf(path: str):
    return os.path.dirname(path)

def installExt(dest:str, source:str):
    path_to_bashrc = os.path.expanduser(dest)
    lines: List[str] = []
    ignoreLine = False
    for line in open(path_to_bashrc):
        line = line.replace("\r", "")
        line = line.replace("\n", "")
        if line == BEGIN_STR:
            ignoreLine = True
        elif line == END_STR:
            ignoreLine = False
        elif not ignoreLine:
            lines.append(line)

    SCRIPT_DIR = dirOf(os.path.abspath(__file__))

    if (not lines[len(lines)-1] == ""):
        lines.append("")

    lines.append(BEGIN_STR)
    lines.append(f"TOOLS_PATH={SCRIPT_DIR}")
    for line in open(os.path.expanduser(source)):
        line = line.replace("\r", "")
        line = line.replace("\n", "")
        lines.append(line)
    lines.append(f"{END_STR}")
    lines.append("")

    open(path_to_bashrc, "w").write("\n".join(lines))

installExt("~/.zshrc", "zshrc-ext.sh")
