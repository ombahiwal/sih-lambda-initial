import subprocess
command = ['rkhunter', '--check', '--sk']
p = subprocess.Popen(command, stdout=subprocess.PIPE)
print("Running RK Hunter test...")
retcode = p.wait()
file = open('/var/log/rkhunter.log', "r")
text = file.read()
print(text)
