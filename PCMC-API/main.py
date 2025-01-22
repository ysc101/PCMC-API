import subprocess
scripts=["Get_Token.py","ECSPush.py","UpdatePayee.py"]

for script in scripts:
    subprocess.run(["python",script]    )