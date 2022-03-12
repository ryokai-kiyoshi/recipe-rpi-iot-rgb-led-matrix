#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time

import board
import neopixel

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):

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

        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("rpi-rgb-led-matrix/fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        my_text = self.args.text

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            # 0番目をRED指定
            pixels[0] = (255, 0, 0)
            # 1番目をGREEN指定
            pixels[1] = (0, 255, 0)
            # 2番目をBLUE指定
            pixels[2] = (0, 0, 255)
            # 3番目をWHITE指定
            pixels[3] = (255, 255, 255)
            pixels.show()
            time.sleep(0.05)

            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            pixels.fill((0, 0, 0))
            pixels.show()


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
