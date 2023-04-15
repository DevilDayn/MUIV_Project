import win32api

monitor = win32api.EnumDisplayMonitors()[0][0]


screen_width = int(win32api.GetMonitorInfo(monitor)['Monitor'][2])
screen_height = int(win32api.GetMonitorInfo(monitor)['Monitor'][3])

