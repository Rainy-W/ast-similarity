import os
import glob
import subprocess
from tqdm import tqdm



def mkJsonFile(dir_name, file_name):
    dir_path = os.path.join(os.getcwd()+'/Jsonfile', dir_name)
    # print(os.getcwd(), dir_path)
    folder = os.path.exists(dir_path)

    if not folder:
        os.mkdir(dir_path)
    else:
        print("There is a same folder")
    
    fn = file_name[0:-4]
    file_path = dir_path + "/" + fn + '.json'
    fp = open(file_path, 'w')
    fp.close()

    return file_path



def get_php_path(dir_name):
    """
    Input:
        dir_name: the name of directory to search

    Output:
        file_paths: all paths of .php file in directory
    """
    # content = os.walk(dir_name)

    content = os.walk(os.getcwd()+"/phpfile/"+dir_name)
    php_paths = []
    json_paths = []
    for path, dir_list, file_list in content:
        for file_name in file_list:
            file_path = os.path.join(path, file_name)
            if file_path.endswith(".php") and os.path.isfile(file_path):
                php_paths.append(file_path)
                json_path = mkJsonFile(dir_name, file_name)
                json_paths.append(json_path)
            # paths = glob.glob(path + "/**/*.php", recursive=True)
    return php_paths, json_paths

def convert_to_Json(php_paths, json_paths):
    for php, json in zip(php_paths, json_paths):
        # command = ["php", "../phpjson.php", php, json]
        # command = ["php", "phpjson.php", php, json]
        # subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        subprocess.run("php phpjson.php {0} {1}".format(php, json), shell=True, stdout=subprocess.PIPE)



# os.chdir("./unzipped/")
# kits = os.listdir("../unzipped/")
# print(os.getcwd())
kits_php = os.listdir(os.getcwd()+"/phpfile/")
# print(kits)
for kit in kits_php:
    php_paths, json_paths = get_php_path(kit)
    convert_to_Json(php_paths, json_paths)



    