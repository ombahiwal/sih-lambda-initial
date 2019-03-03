import subprocess
command = ['rkhunter', '--check', '--sk']

p = subprocess.Popen(command, stdout=subprocess.PIPE)
print("Running RK Hunter test...")
text = p.stdout.read()
print(text)
retcode = p.wait()
