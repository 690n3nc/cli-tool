import sys, os

arg = ""
if len(sys.argv) == 2 and sys.argv[0] == "+":
    if sys.argv[1] == "c":
        temp = open("/home/<<USER>>/.cli-tool/c_template", "r").read()
        f = open("main.c", "w")
        f.write(temp)
        f.close()
        
    elif sys.argv[1] == "cpp":
        temp = open("/home/<<USER>>/.cli-tool/cpp_template", "r").read()
        f = open("main.cpp", "w")
        f.write(temp)
        f.close()
        
    elif sys.argv[1] == "java":
        temp = open("/home/<<USER>>/.cli-tool/java_template", "r").read()
        f = open("Main.java", "w")
        f.write(temp)
        f.close()
        
    else:
        print("-\nUNVALID INPUT\n-")
        sys.exit()
else:
    print("there is only two extra needed and first arg must be +.")
    sys.exit()
    
os.system( arg )
