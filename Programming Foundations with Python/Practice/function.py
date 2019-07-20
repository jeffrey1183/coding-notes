import webbrowser
import time

total_break = 3
break_down = 0

print("This program started on"+ time.ctime())
while break_down < total_break:
    time.sleep(3)
    webbrowser.open("https://www.youtube.com/watch?v=XuvF7HF_kLM&list=PLic4-kKWu0iCeIn4zan5709ojhvim1659&index=5&t=0s")
    break_down += 1



