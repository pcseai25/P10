import json
import os
from psutil import disk_partitions
# import wmi
class Work:
    """TODO Make a model that performs a task and make it work in a Thread not in main class

    Args:
        Prop (class): Primary Class
    """    
    def open_folder(self, sentence):
        # Disc name keywords
        disc_keywords = ["disc", "disk"]
        
        # Extracting disc name and folder name
        disc_name = None
        folder_name = None
        words = sentence.split()
        for i in range(len(words)):
            if words[i] in disc_keywords and i+1 < len(words):
                disc_name = words[i+1]
            elif words[i] == "folder" and i+1 < len(words):
                folder_name = words[i+1]
        return [disc_name,folder_name]


    def search_directory_in_disk(self, directory_path, target_directory):
        for root, dirs, files in os.walk(directory_path):
            if target_directory in dirs:
                target_directory_path = os.path.join(root, target_directory)
                print(f"The directory '{target_directory}' is found at '{target_directory_path}'.")
                os.startfile(target_directory_path)
                return True
        return False

    def open_(self, sentence):
        disk_path = self.open_folder(sentence)[0]+':/'  # Specify the disk path you want to traverse
        target_directory = self.open_folder(sentence)[1]   # Specify the directory name to search and open

        if os.path.isdir(disk_path):
            if not self.search_directory_in_disk(disk_path, target_directory):
                print(f"The directory '{target_directory}' is not found in the disk '{disk_path}'.")
        else:
            print(f"The disk path '{disk_path}' is not valid.")

    # def open_(self,app_name=""):
    #     app_name = set(app_name.split())
    #     with open("FileIndex.json",'r',encoding="utf-8") as AppList:
    #         path, c = '', 0.0
    #         for apps in json.load(AppList):
    #             app = set(apps['name'].split())
    #             freq = len(app.intersection(app_name))/len(app)
    #             if freq > c:
    #                 c=freq
    #                 path = path.replace(path, apps['path'])
    #         if path:
    #             os.startfile(path)
    #         else:
    #             print("Can't find a proper application")
    #         AppList.close()

    def get_disk_info(self):
        disks = disk_partitions(all=True)
        return [disk.device for disk in disks]
    
  