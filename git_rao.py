import sys, os

if len(sys.argv) == 3:
	arg = f"git remote add origin https://github.com/{ sys.argv[1] }/{ sys.argv[2] }"
	os.system(arg)
else:
	print("there should be 2 extra.")