import sys, os
if len(sys.argv) == 3:
    arg = f"git clone https://github.com/{ sys.argv[1] }/{ sys.argv[2] } { sys.argv[3]}"
elif len(sys.argv) == 2:
    arg = f"git clone https://github.com/{ sys.argv[1] }/{ sys.argv[2] }"

else:
    arg = "echo '2 or 3 extra required'"

os.system(arg)
