import datetime
import time

def is_light_on(t):
    return t >= datetime.time(18, 0) or t < datetime.time(6, 0)

def control_light():
    on_time = datetime.time(18, 0)
    off_time = datetime.time(6, 0)
    try:
        while True:
            now = datetime.datetime.now()
            current = now.time()
            if is_light_on(current):
                status = "ON"
            else:
                status = "OFF"
            print(f"{now.strftime('%H:%M:%S')} - Light: {status}")
            time.sleep(10)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    control_light()
