from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Please enter valid positive values.")
            return

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal Weight"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        result_label.config(
            text=f"Your BMI is: {bmi}\nCategory: {category}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter numeric values only.")

# Main Window
root = Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.config(bg="#E8F6F3")

# Heading
title_label = Label(
    root,
    text="BMI Calculator",
    font=("Arial", 20, "bold"),
    bg="#E8F6F3",
    fg="#2E4053"
)
title_label.pack(pady=20)

# Weight Input
weight_label = Label(
    root,
    text="Enter Weight (kg):",
    font=("Arial", 12),
    bg="#E8F6F3"
)
weight_label.pack()

weight_entry = Entry(
    root,
    font=("Arial", 12),
    width=20
)
weight_entry.pack(pady=10)

# Height Input
height_label = Label(
    root,
    text="Enter Height (meters):",
    font=("Arial", 12),
    bg="#E8F6F3"
)
height_label.pack()

height_entry = Entry(
    root,
    font=("Arial", 12),
    width=20
)
height_entry.pack(pady=10)

# Calculate Button
calc_button = Button(
    root,
    text="Calculate BMI",
    font=("Arial", 12, "bold"),
    bg="#48C9B0",
    fg="white",
    command=calculate_bmi
)
calc_button.pack(pady=20)

# Result Label
result_label = Label(
    root,
    text="",
    font=("Arial", 13, "bold"),
    bg="#E8F6F3",
    fg="#1B4F72"
)
result_label.pack(pady=20)

# Run Application
root.mainloop()
