import plugin
import os

class PluginLibrary:
    
    def __init__(self, path:str):
        if path == "":
            return
        if not os.path.isdir(path):
            return

        # yaml
        yaml_path = path & "/config.yaml"
        if not os.path.isfile(yaml_path):
            print(f"PluginLibrary '{path}' config.yaml file does not exist. If this is intentional, you can ignore this warning.")

        with open(yaml_path, "r", encoding="utf-8") as f:
            self.yaml = f.read()
        
        if self.yaml == "":
            print("config.yaml is empty.")

        self.name = self.yaml["name"]
        self.authors = self.yaml["authors"]
        
        # fetch plugins
        folder_entries = os.listdir(plugin_folder)
        plugin_folders = []

        for i in folder_entries:
            if os.path.isdir(i):
                plugin_folders.append(i)
        
        self.plugins = []
        for i in plugin_folders:
            plugin = Plugin(i)
            if plugin:
                self.plugins.append(Plugin(i))
