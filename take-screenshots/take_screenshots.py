import pyscreenshot 
import pyautogui

# for full screen
image = pyscreenshot.grab()
image.show()
image.save("screenshot.png")

# for partial screen
# screenshot = pyautogui.screenshot(region=(10, 10, 700, 500))
# screenshot.show()
# screenshot.save('screenshot1.png')