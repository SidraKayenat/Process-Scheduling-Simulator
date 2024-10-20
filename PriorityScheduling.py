import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import Canvas  # Import Canvas from tkinter

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def calculate_priority_scheduling(processes):
    current_time = 0
    gantt_chart = []
    completed_processes = []
    processes.sort(key=lambda x: x.arrival_time)  # Sort by arrival time first for accurate scheduling

    while processes:
        # Get all processes that have arrived by current_time
        ready_queue = [p for p in processes if p.arrival_time <= current_time]
        if ready_queue:
            # Sort by priority (lower value indicates higher priority)
            ready_queue.sort(key=lambda x: x.priority)
            process = ready_queue[0]
            processes.remove(process)

            if current_time < process.arrival_time:
                current_time = process.arrival_time
            process.completion_time = current_time + process.burst_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            gantt_chart.append((process.pid, current_time, process.burst_time))
            current_time = process.completion_time

            completed_processes.append(process)
        else:
            current_time += 1  # If no process is ready, increment the time

    return gantt_chart, completed_processes

def print_process_info(processes):
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


def draw_gantt_chart_colored_priority(gantt_chart, frame):
    fig, gnt = plt.subplots()

    gnt.set_ylim(0, 10)
    gnt.set_xlim(0, sum(burst for _, _, burst in gantt_chart) + max(start for _, start, _ in gantt_chart))

    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')

    gnt.set_yticks([5])
    gnt.set_yticklabels([''])

    gnt.grid(True)

    # Define a wide range of colors
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

    for i, (pid, start, burst) in enumerate(gantt_chart):
        color = colors[i % len(colors)]
        gnt.broken_barh([(start, burst)], (3, 4), facecolors=(color,))
        gnt.text(start + burst / 2, 5, f'P{pid}', ha='center', va='center', color='white', fontsize=12)

    # Embed the plot into Tkinter frame
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def read_processes_from_file(filename):
    processes = []
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
    return processes
