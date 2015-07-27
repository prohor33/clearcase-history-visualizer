import datetime
import pickle
import os
from os import walk
import subprocess

class Node:
    """Contains history about one folder/file"""
    def __init__(self, path):
        self.path = path
        self.childs = []
        self.log = []
        # position for drawing
        self.pos = (0, 0)

    def pickle(self):
        f = open('test_file', 'wb')
        pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        f.close()

    @staticmethod
    def unpickle():
        with open('test_file', 'rb') as f:
            return pickle.load(f)

##root = Node("C:/")
##root.log.append((datetime.datetime(2015, 7, 21, 16, 25), 'ivan'))
##
##n1 = Node("C:/1")
##root.childs.append(n1)
##n1 = Node("C:/2")
##root.childs.append(n1)
##n1 = Node("C:/3")
##root.childs.append(n1)
##n1 = Node("C:/4")
##root.childs.append(n1)
##n1 = Node("C:/5")
##root.childs.append(n1)

#root.pickle()

# test
#data = Node.unpickle()
#print(data.path)

start_path = "D:/SNAPSHOTS/0_rpr_efd_15_0_gladkikh_dependency_next_gen/efd/NGP/source.ui";
old_cwd = os.getcwd()
root = Node(start_path)
max_files_number = 20
max_files_in_one_dir = 4
max_history_length = 2
files_n = 0

def parse_output(output, node):
    str = output.decode('utf8', 'ignore')
    #print("output = ", str)
    str_list = str.split("\n")
    i = 0
    for out in str_list:
        parse_one_string(out, node)
        i = i + 1
        if i > max_history_length:
            break

def parse_one_string(out, node):
    #print("out = ", out)
    if out is "":
        return
    str_list = out.split(" ")
    name = str_list[2]

    date_str = str_list[0]
    from dateutil import parser
    date = parser.parse(date_str)
    print(name , ": ", date)
    node.log.append((date, name))  

def walk_dirs(path, node):
    global files_n, max_files_number
    for (dirpath, dirnames, filenames) in walk(path):
        os.chdir(dirpath)
        files_n = files_n + 1
        if (files_n > max_files_number):
            return

        files_in_curr_dir = 0
        for filename in filenames:
            print("filename = ", filename)
            parse_output(subprocess.Popen(["cleartool", "lshistory", filename],
                                          stdout=subprocess.PIPE).communicate()[0], node)
            files_n = files_n + 1
            if (files_n > max_files_number):
                return
            files_in_curr_dir = files_in_curr_dir + 1
            if (files_in_curr_dir > max_files_in_one_dir):
                break
            
        for dirname in dirnames:
            child_path = dirpath + "/" + dirname
            print("dir = ", child_path)
            child = Node(child_path)
            walk_dirs(child_path, child)
            print("we need to go deeper")
            node.childs.append(child)

##walk_dirs(start_path, root)
##os.chdir(old_cwd)
##root.pickle()
##print(len(root.childs[0].childs))


        
        




