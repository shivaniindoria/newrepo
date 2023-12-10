import pyscreenshot 
import pyautogui
import pygetwindow
# image = pyscreenshot.grab()
# image.show()
# image.save("screenshot.png")


# image = pyscreenshot.grab(bbox=(10, 10, 700, 500))
# image = pyscreenshot.grab(bbox=pyscreenshot.select_area())
# image.show() 
# image.save("screenshort1.png") 


print("Please click and drag to select the area to capture.")
print("Press Enter when finished.")

# Get the coordinates of the starting point
start_x, start_y = pyautogui.position()

# Wait for the user to press Enter to finish selecting the area
input("Press Enter to confirm the selection...")

# Get the coordinates of the ending point
end_x, end_y = pyautogui.position()

# Calculate the coordinates and dimensions of the area
left = min(start_x, end_x)
top = min(start_y, end_y)
width = abs(end_x - start_x)
height = abs(end_y - start_y)

# Capture the specified area of the screen
screenshot = pyautogui.screenshot(region=(left, top, width, height))

# Save the captured screenshot to a file
screenshot.save("screenshot.png")

# Display a message indicating the screenshot has been saved
print("Screenshot saved as 'screenshot.png'")
window = pygetwindow.getWindowsAt(left, top)
if window:
    window[0].drawBorder(left, top, width, height, color=(255, 0, 0), width=3)