import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 64 # 64のLEDを制御

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.010, auto_write=False, pixel_order=ORDER)

# 0番目をRED指定
pixels[0] = (255, 0, 0)
# 1番目をGREEN指定
pixels[1] = (0, 255, 0)
# 2番目をBLUE指定
pixels[2] = (0, 0, 255)
# 3番目をWHITE指定
pixels[3] = (255, 255, 255)
# LEDの状態を更新(ここで点灯)
pixels.show()

time.sleep(1)

# num_pixelsのLEDにBLACK(消灯)指定
pixels.fill((0, 0, 0))
# LEDの状態を更新(ここで消灯)
pixels.show()