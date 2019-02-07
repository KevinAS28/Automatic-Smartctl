import subprocess
import time
def start(executable_file):
    return subprocess.Popen(
        executable_file,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

def read(process):
    return process.stdout.readline()

def write(process, message):
    process.stdin.write(("%s\n"%(message.strip())).encode("utf-8"))
    process.stdin.flush()

def terminate(process):
    process.stdin.close()
    process.terminate()
    process.wait(timeout=0.2)

process = start(["sh"])
inp = ["ls"]
for i in inp:
	time.sleep(0.5)
	write(process, i)
	print(read(process))
#terminate(process)
