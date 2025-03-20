import os
from totex import table_to_tex, img_to_tex

table = [
    ["r1c1", "r1c2", "r1c3"],
    ["r2c1", "r2c2", "r2c3"],
    ["r3c1", "r3c2", "r3c3"],
]

lines = [
    "\\documentclass{article}\n",
    "\\begin{document}\n",
    table_to_tex(table),
    "\\end{document}\n"
]

with open(os.path.join(".", "artifacts", "test_table_to_tex.tex"), "w") as f:
    f.writelines(lines)

lines = [
    "\\documentclass{article}\n",
    "\\usepackage{graphicx}\n",
    "\\begin{document}\n",
    img_to_tex("img"),
    table_to_tex(table),
    "\\end{document}\n"
]

with open(os.path.join(".", "artifacts", "test_table_and_img_to_tex.tex"), "w") as f:
    f.writelines(lines)
