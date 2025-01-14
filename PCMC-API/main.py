import subprocess
script=["Get_Token.py","ECSPush.py"]

for script in script:
    subprocess.run(["python",script])