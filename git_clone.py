import sys, os
arg = f"git clone https://github.com/{ sys.argv[1] }/{ sys.argv[2] }"
os.system(arg)