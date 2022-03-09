import subprocess
import os
import requests
import time
import cv2
import numpy as np
import pyautogui
import asyncio


async def capture_screen():
    SCREEN_SIZE = tuple(pyautogui.size())

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")# XVID - avi, mp4v - mp4
    fps = 24
    name_of_fragment = int(time.time())
    out = cv2.VideoWriter(f"tmp/{name_of_fragment}.mp4", fourcc, fps, (SCREEN_SIZE))
    record_seconds = 5

    for i in range(int(record_seconds * fps)):
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        # cv2.imshow("screenshot", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    # cv2.destroyAllWindows()
    out.release()
    print('record was ended')


async def upload_video():
    # requests.post()
    # await asyncio.sleep(2)
    print("asdasd")


def main():
    for i in range(2):
        asyncio.run(capture_screen())
        asyncio.run(upload_video())


if __name__ == '__main__':
    main()