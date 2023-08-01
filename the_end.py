f = open("/home/<<USER>>/.bashrc", "r")
lines = f.readlines()
f.close()


i = 0
while i < 18:
    lines.pop(-1)
    i += 1

new_str="\n"
for c_b in lines:
    new_str += c_b

f = open("/home/<<USER>>/.bashrc", "w")
f.write(new_str)
f.close()
