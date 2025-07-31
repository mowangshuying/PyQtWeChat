from sigleton import *
import json

@singleton
class ConfigUtils:
    def __init__(self):
        self.configPath = "./config/config.json"
        # self.config = self.loadConfig()
        self.loadConfig()

    def loadConfig(self):
        """Load configuration from a file."""
        try:
            with open(self.configPath, 'r', encoding='utf-8') as file:
                self.config = json.load(file)  # Load the configuration into self.config
        except Exception as e:
            print(f"Error loading config: {e}")

    def saveConfig(self):
        """Save configuration to a file."""
        try:
            with open(self.configPath, 'w', encoding='utf-8') as file:
                json.dump(self.config, file, indent=4)
        except Exception as e:
            print(f"Error saving config: {e}")

    def getConfig(self, key, default=None):
        """Get a configuration value by key."""
        return self.config.get(key, default)

    def setConfig(self, key, value):
        """Set a configuration value."""
        self.config[key] = value
        self.saveConfig()