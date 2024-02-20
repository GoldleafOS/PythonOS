import webbrowser
import subprocess
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
    subprocess.run(["python3", "kernel.py"])