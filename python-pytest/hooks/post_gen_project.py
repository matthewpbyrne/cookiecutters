import subprocess

if "{{ cookiecutter.use_git }}" == "yes":
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", ".gitignore", ".projections.json", "poetry.toml"])
    subprocess.run(["git", "commit", "-m", "initial commit"])
else:
    subprocess.run(["rm", ".gitignore"])

if "{{ cookiecutter.install_deps }}" == "yes":
    subprocess.Popen(["poetry", "install"], stdout=subprocess.DEVNULL)
