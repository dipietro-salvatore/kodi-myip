import xbmcaddon
import xbmcgui
import requests
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

r = requests.get("http://ipinfo.io/ip")

line1 = "Your public IP address is:"
line2 = r.content
 
xbmcgui.Dialog().ok(addonname, line1, line2)
