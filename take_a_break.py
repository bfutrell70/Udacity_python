import webbrowser
import time

break_count = 0
total_breaks = 3

print("This program started on " + time.ctime())
while break_count < total_breaks:
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=-qlJiGGvPUI")
	break_count = break_count + 1