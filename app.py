import os
from flask import Flask, render_template, request
import subprocess
from typing import List

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/')
def home_page():
    present = get_days_present()
    return render_template('index.html', days=present)


@app.route('/day/<number>/')
def get_day(number):
    template_name = "solution.html"
    problem = readme_convert(number)
    return render_template(template_name, n=number, info=problem)


@ app.route('/day/<number>/get_solution', methods=["GET", "POST"])
def get_solution(number):
    user_in = request.form.get('user_in')
    solution = subprocess.check_output(
        [
            "python3",
            f"day-{number}/solution.py",
            "--input-text",
            user_in
        ]
    )
    return solution


def get_days_present() -> List[str]:
    """Returns the days that are available"""
    contents = os.listdir(basedir)
    matches = []
    for item in contents:
        if "day-" in item:
            matches.append(item)
    matches.sort(key=lambda num: int("".join(filter(str.isdigit, num))))
    result = ""
    for day in matches:
        link = day.split("-")[1]
        result += f"<p><a href='/day/{link}'>Solution {day}</a></p>\n"
    return result[:-1]


def readme_convert(number):
    """
    Parses the readme of day <number> and returns as html
    """
    readme = os.path.join(basedir, f'day-{number}/README.md')
    problem = ""
    block = False
    with open(readme, "r", encoding="utf-8") as file:
        for line in file.read().splitlines():
            split_line = line.split()
            if split_line:
                if split_line[0] == "#":  # header
                    problem += f"<h1>{line[2:]}</h1>\n"
                elif split_line[0] == "##":  # sub header
                    if split_line[1] == "Tests":  # ignore all after this line
                        break
                    problem += f"<h2>{line[3:]}</h2>\n"
                elif "```txt" == split_line[0]:  # block of text
                    problem += "<pre><code>"
                    block = True
                elif "```" == split_line[0]:  # end of block of text
                    problem += "</code></pre>"
                    block = False
                elif split_line[0][-1] == ".":  # numbered list
                    if problem[-5:] == "</ol>":
                        problem = problem[:-5]
                    else:
                        problem += "<ol>\n"
                    problem += f"<li>{' '.join(split_line[1:])}</li>\n</ol>"
                elif split_line[0][:2] == "**":  # bold text
                    problem += f"<strong>{line[2:-2]}</strong>"
                elif split_line[0] == "-":  # list
                    if problem[-5:] == "</ul>":
                        problem = problem[:-5]
                    else:
                        problem += "<ul>\n"
                    problem += f"<li>{' '.join(split_line[1:])}</li>\n</ul>"
                else:
                    if block or line == "":
                        problem += f"{line}\n"
                    else:
                        problem += f"\n<p>{line}</p>\n"
    return problem


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
