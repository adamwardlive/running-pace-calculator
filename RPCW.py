import tkinter as tk
import datetime

class MyWindow:
    def __init__(self, master):
        self.master = master
        master.title("Running Pace Calculator")

        # Create distance label and field
        self.label1 = tk.Label(master, text="Distance (KM):")
        self.label1.grid(row=0, column=0)

        self.entry1 = tk.Entry(master)
        self.entry1.grid(row=0, column=1)

        # Create time label and field
        self.label2 = tk.Label(master, text="Time (M:SS):")
        self.label2.grid(row=1, column=0)

        self.entry2 = tk.Entry(master)
        self.entry2.grid(row=1, column=1)

        # Create calculate button
        self.button = tk.Button(master, text="Calculate", command=self.calculate)
        self.button.grid(row=2, column=0, columnspan=2)

        # Create output label
        self.output = tk.Label(master, text="")
        self.output.grid(row=3, column=0, columnspan=2)

    def calculate(self):
        # Get input values
        distance_in = float(self.entry1.get())
        pace_in = self.entry2.get()


        distance = int(distance_in)
        mins_in, secs_in = pace_in.split(':') # Split the string into minutes and seconds


        pace_minutes = int(mins_in)
        pace_seconds = int(secs_in)

        # Calculate the pace in seconds per kilometer
        pace_seconds_total = pace_minutes * 60 + pace_seconds

        # Calculate the total run time in seconds
        duration = pace_seconds_total * distance

        # Convert to timedelta object
        delta = datetime.timedelta(seconds=duration)

        # Extract hours, minutes, and seconds
        hours = delta.seconds // 3600
        minutes = (delta.seconds // 60) % 60
        seconds = delta.seconds % 60
        

        # Format the output string
        if minutes >= 60:
            hours += 1
            minutes -= 60

        # Perform calculation
        #result = input1 + input2

        # Update output label
        self.output.config(text=f"Total Time: {hours}:{minutes:02d}:{seconds:02d}")
        distance = int(distance_in)
        mins_in, secs_in = pace_in.split(':') # Split the string into minutes and seconds


        pace_minutes = int(mins_in)
        pace_seconds = int(secs_in)

        # Calculate the pace in seconds per kilometer
        pace_seconds_total = pace_minutes * 60 + pace_seconds

        # Calculate the total run time in seconds
        duration = pace_seconds_total * distance

        # Convert to timedelta object
        delta = datetime.timedelta(seconds=duration)

        # Extract hours, minutes, and seconds
        hours = delta.seconds // 3600
        minutes = (delta.seconds // 60) % 60
        seconds = delta.seconds % 60
        

        # Format the output string
        if minutes >= 60:
            hours += 1
            minutes -= 60

        # Perform calculation
        #result = input1 + input2

        # Update output label
        self.output.config(text=f"Total Time: {hours}:{minutes:02d}:{seconds:02d}")

# Create main window
root = tk.Tk()

# Create instance of MyWindow class
my_window = MyWindow(root)

# Start main event loop
root.mainloop()
