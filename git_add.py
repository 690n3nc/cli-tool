import sys, os
arg = ""
if len(sys.argv) > 1:
	if len(sys.argv[1]) >= 2:
		arg = f"git add {sys.argv[1]}"
	else:
		arg = f"git add -A"

	os.system(arg)

else:
	arg = f"git add -A"

	os.system(arg)