import sys, os
arg = ""
if len(sys.argv) > 1:
	if len(sys.argv[1]) >= 2:
		arg = f"git checkout {sys.argv[1]}"
	else:
		arg = f"git checkout"

	os.system(arg)

else:
	arg = f"git checkout"
	os.system(arg)

