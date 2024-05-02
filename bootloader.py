
print("[Fastboot]booting")
import subprocess
fastboot = input("Bash and GUI:")  
#fastboot = "Bash"    
if fastboot == "GUI":
    subprocess.run(["python", "GUI.py"])
if fastboot == "Bash":
    subprocess.run(["python3", "kernel.py"])

