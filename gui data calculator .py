import tkinter as tk
from tkinter import ttk

def calculate_equivalents():
    try:
        gb_value = float(entry_gb.get())
        if gb_value <= 0:
            result_label.config(text="Please enter a valid value for gigabytes.")
            return

        # Calculate equivalents
        mb_value = gb_value * 1024
        kb_value = mb_value * 1024
        bytes_value = kb_value * 1024
        bits_value = bytes_value * 8

        # Display the result
        result_text = (
            f"Equivalent Megabytes: {mb_value:.2f} MB\n"
            f"Equivalent Kilobytes: {kb_value:.2f} KB\n"
            f"Equivalent Bytes: {bytes_value:.2f} bytes\n"
            f"Equivalent Bits: {bits_value:.2f} bits"
        )
        result_label.config(text=result_text)

    except ValueError:
        result_label.config(text="Please enter a valid value for gigabytes.")

# Create the main window
root = tk.Tk()
root.title("Storage Size Converter")

# Create and configure the main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# GB Entry
gb_label = ttk.Label(main_frame, text="Enter the value in gigabytes:")
gb_label.grid(column=0, row=0, sticky=tk.W, pady=5)
entry_gb = ttk.Entry(main_frame, width=10)
entry_gb.grid(column=1, row=0, padx=10, pady=5)

# Calculate Button
calculate_button = ttk.Button(main_frame, text="Calculate", command=calculate_equivalents)
calculate_button.grid(column=0, row=1, pady=10, columnspan=2)

# Result Label
result_label = ttk.Label(main_frame, text="")
result_label.grid(column=0, row=2, pady=10, columnspan=2)

# Run the main loop
root.mainloop()
