import tkinter as tk
root = tk.Tk()
root.title("Manual Traffic Signals at Crossroad")
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.create_rectangle(100, 50, 400, 350, fill="gray")

canvas.create_line(250, 50, 250, 350, fill="white", width=15)
canvas.create_line(100, 200, 400, 200, fill="white", width=15)


signal_colors = ["red", "red", "red", "red"]


signal_timer = None


def reset_signals():
    for i in range(4):
        signal_colors[i] = "red"
    update_signals()


def execute():
    execution_delay = int(execution_delay_entry.get())
    duration = int(duration_entry.get())
    green_signal = int(green_signal_choice.get()) - 1


    signal_colors[green_signal] = "green"
    update_signals()

    def set_signals_red():
        for i in range(4):
            if i != green_signal:
                signal_colors[i] = "red"
        update_signals()

    root.after(execution_delay * 1000, set_signals_red)
    root.after((execution_delay + duration) * 1000, reset_signals)


def toggle_signal(signal_index):
    if signal_colors[signal_index] == "red":
        signal_colors[signal_index] = "green"
    else:
        signal_colors[signal_index] = "red"
    update_signals()


def update_signals():
    canvas.delete("signal")  
    for i, color in enumerate(signal_colors):
        x, y = signal_coordinates[i]
        canvas.create_oval(x, y, x + 20, y + 20, fill=color, tags="signal")


signal_coordinates = [(240, 150), (240, 230), (200, 190), (280, 190)]  


signal_buttons = []

for i in range(4):
    button = tk.Button(root, text=f"Toggle Signal {i+1}", command=lambda i=i: toggle_signal(i))
    button.pack()
    signal_buttons.append(button)


green_signal_label = tk.Label(root, text="Select Green Signal:")
green_signal_label.pack()

green_signal_choice = tk.StringVar(root)
green_signal_choice.set("1")

green_signal_menu = tk.OptionMenu(root, green_signal_choice, "1", "2", "3", "4")
green_signal_menu.pack()

#delay inp. 
execution_delay_label = tk.Label(root, text="Execution Delay (seconds):")
execution_delay_label.pack()

execution_delay_entry = tk.Entry(root)
execution_delay_entry.pack()

#dur. inp.  
duration_label = tk.Label(root, text="Duration (seconds):")
duration_label.pack()

#vedant.rai
duration_entry = tk.Entry(root)
duration_entry.pack()

#exec
execute_button = tk.Button(root, text="Execute", command=execute)
execute_button.pack()

#abort
reset_button = tk.Button(root, text="ABORT!!!", command=reset_signals)
reset_button.pack()

update_signals()

root.mainloop()