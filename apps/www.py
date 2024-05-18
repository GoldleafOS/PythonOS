import webbrowser
import subprocess
import os
print("""
       _____
   ,-:` \;',`'-, 
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-' /
  `.   ;/         .'
    `'-._____.、、/
######################################
   PYWWW     PythonOS s WWW
######################################
""")
www = input("mode:")
if www == "搜索" :
    webbrowser.open("www.bing.com")
if "www" or ".com" in www :
    webbrowser.open(www)
else:
    print("error")
    pyos_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'apps', 'app_api.py')
    subprocess.run(["python3", "app_api.py"])