__author__ = 'Jamie'

from tkinter import *
import time
from ball import Ball
from paddle import Paddle

tk = Tk()
tk.title("BounceBall")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

while 1:
    if paddle.button_down is True and ball.hit_bottom is False:
        ball.draw()
        paddle.draw()

    if ball.hit_bottom is True:
        canvas.create_text(250, 200, text="Game Over")
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
