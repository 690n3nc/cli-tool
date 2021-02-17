import sys, os
arg = ""
if len(sys.argv) > 1:
	if len(sys.argv[1]) >= 2:
		arg = f"git rm {sys.argv[1]}"
	else:
		arg = f"echo 'this is not enough.'"

	os.system(arg)
	