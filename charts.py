import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import data_fetch

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1+radius, y1,
        x1+radius, y1,
        x2-radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1+radius,
        x1, y1
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

def create_main_window(file_path):
    root = tk.Tk()
    root.title("Performance Comparison")
    root.state('zoomed')
    global waiting_time, turnaround_time
    waiting_time, turnaround_time = data_fetch(file_path)
    return root

def create_side_frame(root):
    side_frame = tk.Frame(root, bg="#404040")
    side_frame.pack(side="top", fill="x")

    label = tk.Label(side_frame, text="Performance Charts", bg="#404040", fg="#FFF", font=("Arial", 15, "bold"))
    label.pack(pady=20, padx=0, side="left")
    return side_frame

def create_charts_frame(root):
    charts_frame = tk.Frame(root)
    charts_frame.pack(fill="both", expand=True)
    return charts_frame

def create_charts(charts_frame):
    plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#d68102", "#F4C2C2", "#FFC3CB"]
    )
    fig1, ax1 = plt.subplots()
    ax1.plot(list(waiting_time.keys()), list(waiting_time.values()))
    ax1.set_title("Waiting Time Graph")
    ax1.set_xlabel("Algorithms")
    ax1.set_ylabel("Avg Waiting Times")
    
    fig2, ax2 = plt.subplots()
    ax2.plot(list(turnaround_time.keys()), list(turnaround_time.values()))
    ax2.set_title("Turnaround Time Graph")
    ax2.set_xlabel("Algorithms")
    ax2.set_ylabel("Avg Turnaround Times")

    canvas1 = FigureCanvasTkAgg(fig1, charts_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

    canvas2 = FigureCanvasTkAgg(fig2, charts_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side="right", fill="both", expand=True)

def create_text_frame(root):
    text_frame = tk.Frame(root, bg="#FFF")
    text_frame.pack(fill="both", expand=True)
    return text_frame

def create_custom_names():
    return {
        'FCFS': 'First Come First Serve (FCFS)',
        'SJF': 'Shortest Job First (SJF)',
        'RR': 'Round Robin (RR)',
        "MLQ" : "Multi-Level Queues (MLQ)",
        'PS': 'Priority Scheduling (PS)'
    }

def build_data_strings(custom_names):
    max_name_length = max(len(name) for name in custom_names.values())
    max_time_length = max(len(str(time)) for time in list(waiting_time.values()) + list(turnaround_time.values()))

    data_str_wait = "\nWaiting Time Data:\n"
    for alg, time in waiting_time.items():
        data_str_wait += f"{custom_names[alg]:<{max_name_length}}: {time:>{max_time_length}}\n"

    data_str_turn = "\nTurnaround Time Data:\n"
    for alg, time in turnaround_time.items():
        data_str_turn += f"{custom_names[alg]:<{max_name_length}}: {time:>{max_time_length}}\n"
    
    return data_str_wait, data_str_turn

def create_data_canvases(text_frame, data_str_wait, data_str_turn):
    canvas_wait = tk.Canvas(text_frame, bg="#FFF", highlightthickness=0)
    canvas_turn = tk.Canvas(text_frame, bg="#FFF", highlightthickness=0)

    rect_wait = create_rounded_rectangle(canvas_wait, 65, 0, 600, 130, radius=20, fill="#404040")
    rect_turn = create_rounded_rectangle(canvas_turn, 65, 0, 600, 130, radius=20, fill="#404040")

    data_label_wait = tk.Label(canvas_wait, text=data_str_wait, bg="#404040", fg="#FFF", font=("Arial", 12))
    data_label_turn = tk.Label(canvas_turn, text=data_str_turn, bg="#404040", fg="#FFF", font=("Arial", 12))

    canvas_wait.create_window(330, 55, window=data_label_wait)
    canvas_turn.create_window(330, 55, window=data_label_turn)

    canvas_wait.pack(side="left", padx=20, pady=0, fill="both", expand=True)
    canvas_turn.pack(side="right", padx=20, pady=0, fill="both", expand=True)

def main(file_path):
    root = create_main_window(file_path)
    create_side_frame(root)
    charts_frame = create_charts_frame(root)
    create_charts(charts_frame)
    text_frame = create_text_frame(root)
    custom_names = create_custom_names()
    data_str_wait, data_str_turn = build_data_strings(custom_names)
    create_data_canvases(text_frame, data_str_wait, data_str_turn)
    root.mainloop()

if __name__ == "__main__":
    main()
