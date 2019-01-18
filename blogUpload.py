
import subprocess
import datetime

subprocess.Popen("/usr/bin/git add *", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
subprocess.Popen("/usr/bin/git commit -m auto push at " + str(datetime.datetime.now()), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate() # 加上当前系统的时间
subprocess.Popen("/usr/bin/git push", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
