import subprocess
import os
print("hello python!")

api_path = os.path.join(os.path.dirname(__file__), 'PythonOSsys', 'app_api.py')

subprocess.run(['python', api_path])