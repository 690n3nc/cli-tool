import sys, os
arg = ""
if len(sys.argv) > 1:
	if len(sys.argv[1]) >= 2:
		arg = f"git branch {sys.argv[1]}"
	else:
		arg = f"git branch"

	os.system(arg)

else:
	arg = f"git branch"
	os.system(arg)