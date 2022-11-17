import glob
import os
import subprocess

# Possible TODOs - use_git
# - init git
# - create new branch and add
# if "cookiecutter.use_git" == "yes":
#     subprocess.run(["git", "init"])
#     subprocess.run(["git", "add", ".gitignore", ".projections.json", "poetry.toml"])


if "{{ cookiecutter.hooks_ext }}" == "SKIP!":
    subprocess.run(["rm", "-rf", "hooks"])


if "{{ cookiecutter.readme_ext }}" == "SKIP!":
    for fp in glob.glob("**/README.*", recursive=True):
        os.remove(fp)
