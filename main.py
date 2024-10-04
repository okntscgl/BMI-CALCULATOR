from tkinter import *

window = Tk()
window.title("BMI CALCULATER")
window.minsize(width=400, height=400)
window.config(bg="plum1")


def calculate_bmi():
    try:
        height = float(entry_2.get())
        weight = float(entry_1.get())
        bmi = round(weight / (height / 100) ** 2, 2)
        label_3.config(text=f"Your BMI is {bmi:.2f}")

        if bmi < 16:
            label_4.config(text="Severe Thinness")
        elif bmi <= 17:
            label_4.config(text="Moderate Thinness")
        elif bmi <= 18.5:
            label_4.config(text="Mild Thinness")
        elif bmi <= 25:
            label_4.config(text="Normal")
        elif bmi <= 30:
            label_4.config(text="Overweight")
        elif bmi <= 35:
            label_4.config(text="Obese Class I !")
        elif bmi <= 40:
            label_4.config(text="Obese Class II !")
        else:
            label_4.config(text="Obese Class III !")

    except ValueError:
        label_3.config(text="Please enter numbers only!")



label_1 = Label(text="Enter Your Weight (kg)", font=('Geometric', 10, "normal"))
label_1.config(fg="black")
label_1.config(bg="plum1")
label_1.pack()
label_1.config(padx=0, pady=30)

entry_1 = Entry(width=10)
entry_1.pack()
entry_1.place(x=160, y=60)

label_2 = Label(text="Enter Your Height (cm)", font=('Geometric', 10, "normal"))
label_2.config(fg="black")
label_2.config(bg="plum1")
label_2.pack()
label_2.config(padx=0, pady=20)

label_3 = Label(text="", font=('Geometric', 10, 'normal'))
label_3.config(fg="black")
label_3.config(bg="plum1")
label_3.pack()
label_3.config(padx=0, pady=80)

label_4 = Label(text="", font=('Geometric', 10, 'normal'))
label_4.config(fg="black")
label_4.config(bg="plum1")
label_4.pack()
label_4.place(x=155, y=240)


entry_2 = Entry(width=10)
entry_2.pack()
entry_2.place(x=160, y=130)


button = Button(text="Calculate", font=('Geometric', 10, "normal",))
button.config(bg="plum2")
button.config(command=calculate_bmi)
button.pack()
button.place(x=160, y=170)

window.mainloop()