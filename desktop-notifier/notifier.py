from plyer import notification

def desktop_notifier(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Desktop Notifier',
        timeout=4 
    )

if __name__ == "__main__":
    title = "Hello"
    message = "This is a desktop notification!"

    desktop_notifier(title, message)
