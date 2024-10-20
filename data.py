import tkinter as tk
from tkinter import filedialog
from FCFS import calculate_fcfs, print_process_info as fcfs_info, read_processes_from_file as fcfs_print
from MLQS import calculate_mlfq,print_process_info as mlqs_info,read_processes_from_file as mlqs_print
from RoundRobin import calculate_round_robin,print_process_info as rr_info,read_processes_from_file as rr_print
from SJF import calculate_sjf,print_process_info_sjf as print_process_info_sjf,read_processes_from_file as sjf_print
from PriorityScheduling import calculate_priority_scheduling,print_process_info as ps_info,read_processes_from_file as ps_print


def data_fetch(file_path):
    processes_fcfs = fcfs_print(file_path)
    processes_mlfq = mlqs_print(file_path)
    processes_rr = rr_print(file_path)
    processes_sjf = sjf_print(file_path)
    processes_ps = ps_print(file_path)
    if processes_fcfs and processes_mlfq and processes_ps and processes_rr and processes_sjf:
        processes_fcfs.sort(key=lambda x: x.arrival_time)
        gantt_chart = calculate_fcfs(processes_fcfs)
        global avg_turnaround_time,avg_waiting_time
        output, avg_turnaround_time,avg_waiting_time = fcfs_info(processes_fcfs)

        processes_mlfq.sort(key=lambda x: x.arrival_time)
        gantt_chart, completed_processes = calculate_mlfq(processes_mlfq, 4,8)
        global avg_turnaround_time1,avg_waiting_time1
        output, avg_turnaround_time1,avg_waiting_time1 = mlqs_info(completed_processes)


        processes_rr.sort(key=lambda x: x.arrival_time)
        gantt_chart, completed_processes = calculate_round_robin(processes_rr, 5)
        global avg_turnaround_time2,avg_waiting_time2
        output,avg_turnaround_time2,avg_waiting_time2=rr_info(completed_processes)


        gantt_chart, completed_processes = calculate_sjf(processes_sjf)
        global avg_turnaround_time3,avg_waiting_time3
        output, avg_turnaround_time3,avg_waiting_time3=print_process_info_sjf(completed_processes)


        gantt_chart, completed_processes = calculate_priority_scheduling(processes_ps)
        global avg_turnaround_time4,avg_waiting_time4
        output, avg_turnaround_time4,avg_waiting_time4=ps_info(completed_processes)
        global waiting_time
        waiting_time = {
        "FCFS": avg_waiting_time,
        "SJF" : avg_waiting_time3,
        "MLQ" : avg_waiting_time1,
        "RR": avg_waiting_time2,
        "PS": avg_waiting_time4
        }
        global turnaround_time
        turnaround_time = {
        "FCFS" : avg_turnaround_time,
        "SJF" : avg_turnaround_time3,
        "MLQ" : avg_turnaround_time1,
        "RR": avg_turnaround_time2,
        "PS": avg_turnaround_time4
        }
    else:
        print("No valid process data found. Please check the input file.")
    
    return waiting_time,turnaround_time