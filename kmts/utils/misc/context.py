#
from threading import Lock


class Context:
    def __init__(self):
        self.playerUpgradeAwaits = dict()
        self.playerLevelsConfigFileContent = dict()
        self.configFileContent = dict()

        self.upgradeProcessing = Lock()
        self.saveLock = Lock()
        self.upgrade = Lock()
