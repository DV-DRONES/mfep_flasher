import os
from plugin import Plugin

class PluginFetcher:

    def __init__(self, plugin_folder:str):
        if os.path.isdir(plugin_folder):
            return

        folder_entries = os.listdir(plugin_folder)
        plugin_folders = []

        for i in folder_entries:
            if os.path.isdir(i):
                plugin_folders.append(i)
        
        plugins = []
        for i in plugin_folders:
            plugin = Plugin(i)
            if plugin:
                plugins.append(Plugin(i))
        
