import image_capture as ic
import image_undistort as iu
import pypylon as pylon
# if __name__ == "__main__":
ic.camera_init()
num = 3
for i in range(num):
    ic.camera_capture(str(i))
ic.camera_off()
