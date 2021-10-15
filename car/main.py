import autopilot as autopilot
from camera import get_video_capture
from sio_client import SIOClient

SERVER_ADDRESS = "localhost"
SERVER_PORT = 5000


def main():
    cap = get_video_capture()
    if cap.isOpened():
        while True:
            _, img = cap.read()
            img = autopilot.get_direction(img)
            SIOClient().send_data(img)
        cap.release()
    else:
        print("Unable to open camera")


if __name__ == "__main__":
    SIOClient().setup(f"http://{SERVER_ADDRESS}:{SERVER_PORT}", 5)

    main()
