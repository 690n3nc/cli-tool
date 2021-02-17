import sys, os

if len(sys.argv) == 2:
    if sys.argv[1] == "c":
        temp = open("/home/<<USER>>/.cli-tool/c_template", "r").read()
        f = open("main.c", "w")
        f.write(temp)
        f.close()
	
	    os.system("nano main.c")
        
    elif sys.argv[1] == "cpp":
        temp = open("/home/<<USER>>/.cli-tool/cpp_template", "r").read()
        f = open("main.cpp", "w")
        f.write(temp)
        f.close()
        
        os.system("nano main.cpp")
        
    elif sys.argv[1] == "java":
        temp = open("/home/<<USER>>/.cli-tool/java_template", "r").read()
        f = open("Main.java", "w")
        f.write(temp)
        f.close()
        
        os.system("nano Main.java")
        
    else:
        print("-\nUNVALID INPUT\n-")
        sys.exit()
else:
    print("there is only two extra needed and first arg must be +.")
    sys.exit()
    
