import os
import sys
import xbmc
import time
import xbmcaddon

__addon__ = xbmcaddon.Addon()
__cwd__ = xbmc.translatePath(__addon__.getAddonInfo('path')).decode("utf-8")
__resource__ = xbmc.translatePath(os.path.join(__cwd__, 'resources')).decode("utf-8")

__settings__ = xbmcaddon.Addon("service.history")

Path = __settings__.getSetting('path')

sys.path.append(__resource__)

def getSetting(setting):
	return __addon__.getSetting(setting).strip()

class HistoryHandler(xbmc.Player):
	def __init__ (self):
		xbmc.Player.__init__(self)

	def onPlayBackStarted(self):
		if xbmc.Player().isPlayingVideo():
			self.logToFile()

	def logToFile(self):
		if xbmc.Player().isPlaying():
			if xbmc.Player().isPlayingVideo():
				playedTime = time.strftime("[%m/%d/%Y %H:%M:%S] ")
				currPlayedingPath = xbmc.Player().getPlayingFile()
				f = open(Path,'a')
				f.write(playedTime + currPlayedingPath + "\n")
				f.close()

player_monitor = HistoryHandler()

while not xbmc.abortRequested:
	xbmc.sleep(1000)

del player_monitor
