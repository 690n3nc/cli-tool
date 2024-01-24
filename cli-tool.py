import sys, os, shutil
from getpass import getuser

username = getuser()
gkey = input("your preferred github key:")

#changing files for the user

fl_1 = open("github_key", "w")
fl_1.write(f"your preferred github key:\n\n{gkey}\n")
fl_1.close()

cont = open("+_catch.py", "r").read()

cont = cont.replace("<<USER>>", username)

fl_1 = open("+_catch.py", "w")
fl_1.write(cont)
fl_1.close()


cont = open("the_end.py", "r").read()

cont = cont.replace("<<USER>>", username)

fl_1 = open("the_end.py", "w")
fl_1.write(cont)
fl_1.close()


cont = open("ilkis.sh", "r").read()

cont = cont.replace("~", "/home/{}".format(username))

fl_1 = open("ilkis.sh", "w")
fl_1.write(cont)
fl_1.close()


cont = open("dilkis.sh", "r").read()

cont = cont.replace("~", "/home/{}".format(username))

fl_1 = open("dilkis.sh", "w")
fl_1.write(cont)
fl_1.close()


cont = open("rilkis.sh", "r").read()

cont = cont.replace("~", "/home/{}".format(username))

fl_1 = open("rilkis.sh", "w")
fl_1.write(cont)
fl_1.close()
#---


raw_lines = open("commands", "r").readlines()

fcontent = "\n\n\n\n"

for line in raw_lines:
	if not( line.startswith("^") ) and (len(line) > 3):
		alias, cmd = line.replace("\n", "").split("&")
		alias = alias.replace(" ", "")
		fcontent += f'alias {alias}="{cmd}"\n'


fl_1 = open("/home/{}/.bashrc".format(username), "a")
fl_1.write(fcontent)
fl_1.close()

cp = os.getcwd()
try:
    os.chdir("/home/{}/.cli-tool".format(username))
except:
    os.mkdir("/home/{}/.cli-tool".format(username))

os.chdir(cp)

files = [ 
"git_commit.py",
"git_clone.py",
"git_branch.py",
"git_add.py",
"git_remove.py",
"git_checkout.py",
"git_rao.py",
"+_catch.py",
"java_template",
"cpp_template",
"c_template",
"the_end.py",
"ilkis.sh",
"dilkis.sh",
"rilkis.sh",
"github_key",
"ilkis_logs"
]

for file in files:
	shutil.move(file, "/home/{}/.cli-tool/{}".format(username, file))

try:
	os.system("rm -rf commands cli-tool.py README.md")

	rmdir = os.getcwd()

	if rmdir.endswith("cli-tool") or rmdir.endswith("CLI-TOOL"):
		os.chdir("..")
		arg="rm -rf cli-tool"
		arg2="rm -rf CLI-TOOL"

		os.system(arg)
		os.system(arg2)

except:
	pass

print("cli-tool installed.\nwrite remove-cli-tool to remove.")

