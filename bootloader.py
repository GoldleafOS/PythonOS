
print("[Fastboot]booting")
import subprocess
import os
fastboot = input("Bash and GUI:")  
#fastboot = "Bash"    
if fastboot == "GUI":
    gui_path = os.path.join(os.path.dirname(__file__), 'PythonOSsys', 'GUI.py')
    subprocess.run(["python3", gui_path])
if fastboot == "Bash":
    kernel_path = os.path.join(os.path.dirname(__file__), 'PythonOSsys', 'kernel.py')
    subprocess.run(["python3", kernel_path])

