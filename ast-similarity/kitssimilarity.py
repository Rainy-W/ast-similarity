from astsimilarity import compute_zss_distance, compute_apted_distance
import json
import os


def get_kit_content(kit_name):
    file_paths = []
    content = os.walk(os.getcwd()+"/Jsonfile/"+kit_name)
    for path, dir_list, file_list in content:
        # print(path, file_list)
        for file_name in file_list:
            file_path = os.path.join(path, file_name)
            file_paths.append(file_path)
    return file_paths

def compare_kit(x, y):
    
    x_paths = get_kit_content(x)
    y_paths = get_kit_content(y)
    # print(x_paths, y_paths)
    dist = {}
    for i in range(len(x_paths)):
        for j in range(len(y_paths)):
            # dist.append(compute_apted_distance(x_paths[i], y_paths[j]))
            dist[(i,j)] = compute_apted_distance(x_paths[i], y_paths[j])
            # print(x_paths[i], y_paths[j])
            # print(dist)
    print(dist)

kits_json = os.listdir(os.getcwd()+"/Jsonfile")
print(kits_json)

for i in range(len(kits_json)):
    for j in range(i+1, len(kits_json)):
        compare_kit(kits_json[i], kits_json[j])

