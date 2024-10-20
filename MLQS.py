import tkinter as tk
from collections import deque
import matplotlib.pyplot as plt
from tkinter import Canvas
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.remaining_time = burst_time
        self.start_time = -1

def calculate_mlfq(processes, quantumQ1, quantumQ2):
    current_time = 0
    gantt_chart = []
    q1, q2, q3 = deque(), deque(), deque()

    # Sort processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)

    index = 0
    while index < len(processes) or q1 or q2 or q3:
        # Add processes to Q1 as they arrive
        while index < len(processes) and processes[index].arrival_time <= current_time:
            q1.append(processes[index])
            index += 1

        # Process Q1 (RR with user-defined quantum)
        if q1:
            process = q1.popleft()
            quantum = min(quantumQ1, process.remaining_time)
            if process.start_time == -1:
                process.start_time = current_time
            gantt_chart.append((process.pid, current_time, quantum))
            current_time += quantum
            process.remaining_time -= quantum

            if process.remaining_time > 0:
                q2.append(process)
            else:
                process.completion_time = current_time
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time

        # Process Q2 (RR with user-defined quantum)
        elif q2:
            process = q2.popleft()
            quantum = min(quantumQ2, process.remaining_time)
            if process.start_time == -1:
                process.start_time = current_time
            gantt_chart.append((process.pid, current_time, quantum))
            current_time += quantum
            process.remaining_time -= quantum

            if process.remaining_time > 0:
                q3.append(process)
            else:
                process.completion_time = current_time
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time

        # Process Q3 (FCFS)
        elif q3:
            process = q3.popleft()
            if process.start_time == -1:
                process.start_time = current_time
            gantt_chart.append((process.pid, current_time, process.remaining_time))
            current_time += process.remaining_time
            process.remaining_time = 0
            process.completion_time = current_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time

        # No processes available, advance time
        else:
            current_time += 1

    return gantt_chart, processes

def print_process_info(processes):
    if not processes:
        print("No processes to display.")
        return

    total_turnaround_time = 0
    total_waiting_time = 0

    output = f"{'PID':<15}{'Arrival':<20}{'Burst':<15}{'Priority':<15}{'Completion':<20}{'Turnaround':<20}{'Waiting':<15}\n"
    for process in processes:
        output += f"{process.pid:<20}{process.arrival_time:<20}{process.burst_time:<20}{process.priority:<20}{process.completion_time:<25}{process.turnaround_time:<25}{process.waiting_time:<20}\n"
        total_turnaround_time += process.turnaround_time
        total_waiting_time += process.waiting_time

    avg_turnaround_time = total_turnaround_time / len(processes)
    avg_waiting_time = total_waiting_time / len(processes)

    output += f"\nAverage Turnaround Time: {avg_turnaround_time:.2f}\n"
    output += f"Average Waiting Time: {avg_waiting_time:.2f}\n"
    print(output)
    
    return output, avg_turnaround_time, avg_waiting_time


def draw_gantt_chart_colored(gantt_chart, frame):
    if not gantt_chart:
        print("No processes to display in Gantt chart.")
        return

    # Adjust figure size (width, height) to make it smaller
    fig, gnt = plt.subplots(figsize=(6, 3))  # Adjust width and height as needed

    gnt.set_ylim(0, 10)
    gnt.set_xlim(0, sum(burst for _, _, burst in gantt_chart) + max(start for _, start, _ in gantt_chart))

    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')

    gnt.set_yticks([5])
    gnt.set_yticklabels([''])

    gnt.grid(True)

    # Define a narrower range of colors for a smaller chart
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']

    for i, (pid, start, burst) in enumerate(gantt_chart):
        color = colors[i % len(colors)]
        # Adjust the height of bars (burst) relative to the figure size
        gnt.broken_barh([(start, burst)], (3, 4), facecolors=(color,))
        gnt.text(start + burst / 2, 5, f'P{pid}', ha='center', va='center', color='white', fontsize=8)  # Adjust fontsize

    # Embed the plot into Tkinter frame
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def read_processes_from_file(filename):
    processes = []
    try:
        with open(filename, 'r') as file:
            next(file)  # Skip the header line
            for line_number, line in enumerate(file, start=2):  # Start from line 2 because of header
                parts = line.split()
                if len(parts) != 4:
                    print(f"Error in file {filename} on line {line_number}: Line does not contain exactly four values: {parts}")
                    continue
                try:
                    pid, arrival_time, burst_time, priority = map(int, parts)
                    if pid < 0 or arrival_time < 0 or burst_time <= 0 or priority < 0:
                        print(f"Error in file {filename} on line {line_number}: Line contains invalid values: {parts}")
                        continue
                    processes.append(Process(pid, arrival_time, burst_time, priority))
                except ValueError as e:
                    print(f"Error in file {filename} on line {line_number}: {e}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return processes

