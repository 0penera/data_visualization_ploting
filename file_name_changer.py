import os

path = r"C:\Users\bokseon hwang\Documents\code\matplotlib"
file_list = os.listdir(path)
for name in file_list:
    name_c = name.split("_")[0]
    if name_c == "Corey":
        name_fix = name.split("_")[2]
        os.rename(os.path.join(path, name), os.path.join(path, name_fix))
    

# print(file_list)