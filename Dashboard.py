import tkinter as tk
from tkinter import filedialog, Canvas  # Import Canvas from tkinter
from FCFS import read_processes_from_file as read_processes_from_file_fcfs, calculate_fcfs, print_process_info as print_process_info_fcfs, draw_gantt_chart_colored as draw_gantt_chart_colored_fcfs
from PriorityScheduling import read_processes_from_file as read_processes_from_file_priority, calculate_priority_scheduling, print_process_info as print_process_info_priority, draw_gantt_chart_colored_priority
from RoundRobin import read_processes_from_file as read_processes_from_file_rr, calculate_round_robin, print_process_info as print_process_info_rr, draw_gantt_chart_colored_round_robin 
from MLQS import read_processes_from_file as read_processes_from_file_mlqs , calculate_mlfq, print_process_info as print_process_info_mlqs, draw_gantt_chart_colored as draw_gantt_chart_colored_mlqs
from SJF import  read_processes_from_file as read_processes_from_file_sjf, calculate_sjf, print_process_info_sjf as print_process_info_sjf, draw_gantt_chart_sjf 
from charts import main
# Define the function to switch frames
def show_frame(frame):
    frame.tkraise()

def upload_file_fcfs():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:   
        global processes_fcfs
        processes_fcfs = read_processes_from_file_fcfs(file_path)
        print(f"File uploaded: {file_path}")
        upload_label_fcfs.config(text=f"File uploaded: {file_path.split('/')[-1]}")
        generate_button_fcfs.config(state=tk.NORMAL)

def generate_chart_fcfs():
    if processes_fcfs:
        gantt_chart = calculate_fcfs(processes_fcfs)
        output, avg_turnaround_time, avg_waiting_time = print_process_info_fcfs(processes_fcfs)

        # Clear previous chart if any
        for widget in fcfs_frame.winfo_children():
            if isinstance(widget, Canvas):
                widget.destroy()

        # Create the chart and display it
        draw_gantt_chart_colored_fcfs(gantt_chart, fcfs_frame)

        # Display process information in the GUI
        process_info_label_fcfs.config(text=output)

def upload_file_mlqs():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        global processes_mlqs
        processes_mlqs = read_processes_from_file_mlqs(file_path)
        print(f"File uploaded: {file_path}")
        upload_label_mlqs.config(text=f"File uploaded: {file_path.split('/')[-1]}")
        generate_button_mlqs.config(state=tk.NORMAL)
        
        
def generate_chart_mlqs():
    if processes_mlqs:
        q1 = int(q1_entry.get())
        q2 = int(q2_entry.get())
        gantt_chart,completed_process = calculate_mlfq(processes_mlqs,q1,q2)
        output, avg_turnaround_time, avg_waiting_time = print_process_info_mlqs(processes_mlqs)

        # Clear previous chart if any
        for widget in mlqs_frame.winfo_children():
            if isinstance(widget, Canvas):
                widget.destroy()

        # Create the chart and display it
        draw_gantt_chart_colored_mlqs(gantt_chart, mlqs_frame)

        # Display process information in the GUI
        process_info_label_mlqs.config(text=output)

def upload_file_priority():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        global processes_priority
        processes_priority = read_processes_from_file_priority(file_path)
        print(f"File uploaded: {file_path}")
        upload_label_priority.config(text=f"File uploaded: {file_path.split('/')[-1]}")
        generate_button_priority.config(state=tk.NORMAL)

def generate_chart_priority():
    if processes_priority:
        gantt_chart, completed_processes = calculate_priority_scheduling(processes_priority)
        output, avg_turnaround_time, avg_waiting_time = print_process_info_priority(completed_processes)

        # Clear previous chart if any
        for widget in priority_frame.winfo_children():
            if isinstance(widget, Canvas):
                widget.destroy()

        # Create the chart and display it
        draw_gantt_chart_colored_priority(gantt_chart, priority_frame)

        # Display process information in the GUI
        process_info_label_priority.config(text=output)

def upload_file_rr():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        global processes_rr
        processes_rr = read_processes_from_file_rr(file_path)
        print(f"File uploaded: {file_path}")
        upload_label_rr.config(text=f"File uploaded: {file_path.split('/')[-1]}")
        generate_button_rr.config(state=tk.NORMAL)

def generate_chart_rr():
    if processes_rr:
        time_quantum = int(time_quantum_entry.get())
        gantt_chart, completed_processes = calculate_round_robin(processes_rr, time_quantum)
        output, avg_turnaround_time, avg_waiting_time = print_process_info_rr(completed_processes)

        # Clear previous chart if any
        for widget in roundRobin_frame.winfo_children():
            if isinstance(widget, Canvas):
                widget.destroy()

        # Create the chart and display it
        draw_gantt_chart_colored_round_robin(gantt_chart, roundRobin_frame)

         # Display process information in the GUI
        process_info_label_rr.config(text=output)

def upload_file_sjf():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        global processes_sjf
        processes_sjf = read_processes_from_file_sjf(file_path)
        print(f"File uploaded: {file_path}")
        upload_label_sjf.config(text=f"File uploaded: {file_path.split('/')[-1]}")
        generate_button_sjf.config(state=tk.NORMAL)

def generate_chart_sjf():
    if processes_sjf:
        gantt_chart, completed_processes = calculate_sjf(processes_sjf)
        output, avg_turnaround_time, avg_waiting_time = print_process_info_sjf(completed_processes)

        # Clear previous chart if any
        for widget in shortestJob_frame.winfo_children():
            if isinstance(widget, Canvas):
                widget.destroy()

        # Create the chart and display it
        draw_gantt_chart_sjf(gantt_chart, shortestJob_frame)

        # Display process information in the GUI
        process_info_label_sjf.config(text=output)

def upload_file_com():
    global file_path_com
    file_path_com = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path_com:
        global processes_com
        processes_com = read_processes_from_file_sjf(file_path_com)
        print(f"File uploaded: {file_path_com}")
        upload_label_com.config(text=f"File uploaded: {file_path_com.split('/')[-1]}")
        generate_button_com.config(state=tk.NORMAL)

def generate_chart_com():
    if processes_com:
        main(file_path_com)

        # Clear previous chart if any
        for widget in comparison_frame.winfo_children():
            if isinstance(widget, Canvas):
                widget.destroy()




# Initialize the main window
root = tk.Tk()
root.geometry("1000x700")

# Define the navigation pane frame
# Define the sidebar color
sidebar_color = '#404040'

# SIDEBAR FRAME
sidebar = tk.Frame(root, bg=sidebar_color)
sidebar.place(relx=0, rely=0, relwidth=0.3, relheight=1)

# BRANDING FRAME (UNIVERSITY LOGO AND NAME)
brand_frame = tk.Frame(sidebar, bg=sidebar_color)
brand_frame.place(relx=0, rely=0, relwidth=1, relheight=0.15)

# Substitute icon with an actual image object if available
icon = tk.PhotoImage(file="logo.png")  # Change to your actual logo file path
uni_logo = icon.subsample(9)
logo = tk.Label(brand_frame, image=uni_logo, bg=sidebar_color)
logo.place(x=20, y=20)

uni_name = tk.Label(brand_frame, text='Process Scheduling', bg=sidebar_color, fg='white', font=("", 15, "bold"))
uni_name.place(x=90, y=35, anchor="w")

uni_name = tk.Label(brand_frame, text='Simulator', bg=sidebar_color, fg='white', font=("", 15, "bold"))
uni_name.place(x=130, y=67, anchor="w")

# SUBMENU FRAME (FOR PLACING SUBMENUS)
submenu_frame = tk.Frame(sidebar, bg=sidebar_color)
submenu_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.85)

# Navigation buttons in the sidebar

btn_fcfs = tk.Button(submenu_frame, text="FIRST COME FIRST SERVED", command=lambda: show_frame(fcfs_frame) , height=3, bg='#828282', fg='white',font=("",10,"bold"))
btn_fcfs.pack(fill='x', padx=0, pady=5)

btn_priority = tk.Button(submenu_frame, text="PRIORITY SCHEDULING", command=lambda: show_frame(priority_frame) , height=3, bg='#828282', fg='white',font=("",10,"bold"))
btn_priority.pack(fill='x', padx=0, pady=5)

btn_roundRobin = tk.Button(submenu_frame, text="ROUND ROBIN", command=lambda: show_frame(roundRobin_frame), height=3, bg='#828282', fg='white',font=("",10,"bold"))
btn_roundRobin.pack(fill='x', padx=0, pady=5)

btn_shortestJob = tk.Button(submenu_frame, text="SHORTEST JOB FIRST", command=lambda: show_frame(shortestJob_frame) , height=3, bg='#828282', fg='white',font=("",10,"bold"))
btn_shortestJob.pack(fill='x', padx=0, pady=5)

btn_mlqs = tk.Button(submenu_frame, text="MULTI LEVEL QUEUE SCHEDULING", command=lambda: show_frame(mlqs_frame), height=3, bg='#828282', fg='white',font=("",10,"bold"))
btn_mlqs.pack(fill='x', padx=0, pady=5)

btn_comparison = tk.Button(submenu_frame, text="COMPARISON", command=lambda: show_frame(comparison_frame), height=3, bg='#828282', fg='white',font=("",10,"bold"))
btn_comparison.pack(fill='x', padx=0, pady=5)

# Create frames for each algorithm in the content area
fcfs_frame = tk.Frame(root, bg='white')
priority_frame = tk.Frame(root, bg='white')
roundRobin_frame = tk.Frame(root, bg='white')
shortestJob_frame = tk.Frame(root, bg='white')
mlqs_frame = tk.Frame(root, bg='white')
comparison_frame = tk.Frame(root, bg='white')

# Place all frames in the same location (stack them)
for frame in [fcfs_frame, priority_frame, roundRobin_frame, shortestJob_frame, mlqs_frame, comparison_frame]:
    frame.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)


# Add content to FCFS frame
fcfs_label = tk.Label(fcfs_frame, text="FCFS Algorithm", bg='white', font=("Arial", 16, "bold"))
fcfs_label.pack(pady=(20, 10))

fcfs_box_frame = tk.Frame(fcfs_frame, bg='#404040', relief=tk.SUNKEN)
fcfs_box_frame.pack(pady=(10, 20), padx=20, fill='x')

upload_button_fcfs = tk.Button(fcfs_box_frame, text="Upload File",height=1, command=upload_file_fcfs, bg='#FF9738', fg='white', font=("",10,"bold"))
upload_button_fcfs.pack(side=tk.LEFT, padx=10, pady=10)

upload_label_fcfs = tk.Label(fcfs_box_frame, bg='white')
upload_label_fcfs.pack(side=tk.LEFT, padx=10, pady=10)

generate_button_fcfs = tk.Button(fcfs_box_frame, text="Generate Chart", command=generate_chart_fcfs, state=tk.DISABLED, bg='white', fg='black', font=("",10,"bold"))
generate_button_fcfs.pack(pady=10)

process_info_label_fcfs = tk.Label(fcfs_frame, text="", bg='white', font=("Arial", 8), justify=tk.LEFT)
process_info_label_fcfs.pack(pady=(10, 20))

# Add content to Priority Scheduling frame
priority_label = tk.Label(priority_frame, text="Priority Scheduling Algorithm", bg='white', font=("Arial", 16, "bold"))
priority_label.pack(pady=(20, 10))

priority_box_frame = tk.Frame(priority_frame, bg='#404040', relief=tk.SUNKEN)
priority_box_frame.pack(pady=(10, 20), padx=20, fill='x')

upload_button_priority = tk.Button(priority_box_frame, text="Upload File", command=upload_file_priority, bg='#FF9738', fg='white', font=("",10,"bold"))
upload_button_priority.pack(side=tk.LEFT, padx=10, pady=10)

upload_label_priority = tk.Label(priority_box_frame, text="", bg='white')
upload_label_priority.pack(side=tk.LEFT, padx=10, pady=10)

generate_button_priority = tk.Button(priority_box_frame, text="Generate Chart", command=generate_chart_priority, state=tk.DISABLED, bg='white', fg='black', font=("",10,"bold"))
generate_button_priority.pack(pady=10)

process_info_label_priority = tk.Label(priority_frame, text="", bg='white', font=("Arial", 8), justify=tk.LEFT)
process_info_label_priority.pack(pady=(1, 20))

# Add content to Round Robin frame
roundRobin_label = tk.Label(roundRobin_frame, text="Round Robin Algorithm", bg='white', font=("Arial", 16, "bold"))
roundRobin_label.pack(pady=(20, 10))

roundRobin_box_frame = tk.Frame(roundRobin_frame, bg='#404040', relief=tk.SUNKEN)
roundRobin_box_frame.pack(pady=(10, 20), padx=20, fill='x')

upload_button_roundRobin = tk.Button(roundRobin_box_frame, text="Upload File", command=upload_file_rr, bg='#FF9738', fg='white', font=("",10,"bold"))
upload_button_roundRobin.pack(side=tk.LEFT, padx=10, pady=10)

upload_label_rr = tk.Label(roundRobin_box_frame, text="", bg='white')
upload_label_rr.pack(side=tk.LEFT, padx=10, pady=10)

time_quantum_label = tk.Label(roundRobin_box_frame, text="Time Quantum:", bg='white')
time_quantum_label.pack(pady=10)

time_quantum_entry = tk.Entry(roundRobin_box_frame)
time_quantum_entry.pack(pady=10)

generate_button_rr = tk.Button(roundRobin_box_frame, text="Generate Chart", command=generate_chart_rr, state=tk.DISABLED, bg='white', fg='black', font=("",10,"bold"))
generate_button_rr.pack(pady=10)

process_info_label_rr = tk.Label(roundRobin_frame, text="", bg='white', font=("Arial", 8), justify=tk.LEFT)
process_info_label_rr.pack(pady=(10, 20))

# Add content to MLQS frame
mlqs_label = tk.Label(mlqs_frame, text="MLQS Algorithm", bg='white', font=("Arial", 16, "bold"))
mlqs_label.pack(pady=(20, 10))

mlqs_box_frame = tk.Frame(mlqs_frame, bg='#404040', relief=tk.SUNKEN)
mlqs_box_frame.pack(pady=(10, 20), padx=20, fill='x')

upload_button_mlqs = tk.Button(mlqs_box_frame, text="Upload File", command=upload_file_mlqs, bg='#FF9738', fg='white', font=("",10,"bold"))
upload_button_mlqs.pack(side=tk.LEFT, padx=10, pady=10)

upload_label_mlqs = tk.Label(mlqs_box_frame, text="", bg='white')
upload_label_mlqs.pack(side=tk.LEFT, padx=10, pady=10)

q1_frame = tk.Frame(mlqs_box_frame, bg='light gray')
q1_frame.pack(pady=(10, 0))

q1_label = tk.Label(q1_frame, text="Enter Quantum 1", bg='white')
q1_label.pack(side=tk.LEFT, padx=10, pady=10)

# Add an input field for Quantum 1
q1_entry = tk.Entry(q1_frame)
q1_entry.pack(side=tk.LEFT, padx=10, pady=10)

q2_frame = tk.Frame(mlqs_box_frame, bg='light gray')
q2_frame.pack(pady=(10, 20))

q2_label = tk.Label(q2_frame, text="Enter Quantum 2:", bg='white')
q2_label.pack(side=tk.LEFT, padx=10, pady=10)

q2_entry = tk.Entry(q2_frame)
q2_entry.pack(side=tk.LEFT, padx=10, pady=10)

generate_button_mlqs = tk.Button(mlqs_box_frame, text="Generate Chart", command=generate_chart_mlqs, state=tk.DISABLED, bg='white', fg='black', font=("",10,"bold"))
generate_button_mlqs.pack(pady=10)

generate_button_mlqs.pack(anchor=tk.CENTER, pady=10)

process_info_label_mlqs = tk.Label(mlqs_frame, text="", bg='white', font=("Arial", 8), justify=tk.LEFT)
process_info_label_mlqs.pack(pady=(10, 20))

# Add content to Shortest Job First frame
sjf_label = tk.Label(shortestJob_frame, text="Shortest Job First Algorithm", bg='white', font=("Arial", 16, "bold"))
sjf_label.pack(pady=(20, 10))

sjf_box_frame = tk.Frame(shortestJob_frame, bg='#404040', relief=tk.SUNKEN)
sjf_box_frame.pack(pady=(10, 20), padx=20, fill='x')

upload_button_sjf = tk.Button(sjf_box_frame, text="Upload File", command=upload_file_sjf, bg='#FF9738', fg='white', font=("",10,"bold"))
upload_button_sjf.pack(side=tk.LEFT, padx=10, pady=10)

upload_label_sjf = tk.Label(sjf_box_frame, text="", bg='white')
upload_label_sjf.pack(side=tk.LEFT, padx=10, pady=10)

generate_button_sjf = tk.Button(sjf_box_frame, text="Generate Chart", command=generate_chart_sjf, state=tk.DISABLED, bg='white', fg='black', font=("",10,"bold"))
generate_button_sjf.pack(pady=10)

process_info_label_sjf = tk.Label(shortestJob_frame, text="", bg='white', font=("Arial", 8), justify=tk.LEFT)
process_info_label_sjf.pack(pady=(10, 20))

#Add content to the Comparison frame
com_label = tk.Label(comparison_frame, text="Comparison", bg='white', font=("Arial", 16, "bold"))
com_label.pack(pady=(20, 10))

com_box_frame = tk.Frame(comparison_frame, bg='#404040', relief=tk.SUNKEN)
com_box_frame.pack(pady=(10, 20), padx=20, fill='x')

upload_button_com = tk.Button(com_box_frame, text="Upload File", command=upload_file_com, bg='#FF9738', fg='white', font=("",10,"bold"))
upload_button_com.pack(side=tk.LEFT, padx=10, pady=10)

upload_label_com = tk.Label(com_box_frame, text="", bg='white')
upload_label_com.pack(side=tk.LEFT, padx=10, pady=10)

generate_button_com = tk.Button(com_box_frame, text="Generate Chart", command=generate_chart_com, state=tk.DISABLED, bg='white', fg='black', font=("",10,"bold"))
generate_button_com.pack(pady=10)



# Show the first frame initially
show_frame(fcfs_frame)

# Run the application
root.mainloop()
 