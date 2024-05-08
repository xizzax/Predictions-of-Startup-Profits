from joblib import load
import tkinter

RF_model = load('./model_RF.joblib')

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Profit Prediction")
root.geometry("950x600")

# Function to clear input fields after prediction
def clear_entries():
    rd_spend.delete(0, 'end')
    admin.delete(0, 'end')
    marketing.delete(0, 'end')

# Function to predict profit
def predict():
    # Get the values
    rd = float(rd_spend.get())
    ad = float(admin.get())
    mk = float(marketing.get())
    st = state.get()
    c = 0
    f = 0
    if st == "California":
        c = 1
    elif st == "Florida":
        f = 1

    # Make the prediction
    profit = RF_model.predict([[rd, ad, mk, c, f]])

    # Show the prediction
    prediction_label = tk.Label(root, text=f"Predicted Profit: ${profit[0]:.2f}", font=("Times New Roman", 16), bg="#303030", fg="white")
    prediction_label.grid(row=6, column=1, padx=25, pady=5, sticky="ew")

    
    # Clear the input fields
    clear_entries()

# Resize the image
original_image = Image.open("./stock.png")
resized_image = original_image.resize((350, 600), Image.ANTIALIAS)
tk_image = ImageTk.PhotoImage(resized_image, master=root)

# Left column - Image
image_label = tk.Label(root, image=tk_image, bg="#303030")
image_label.image = tk_image
image_label.grid(row=0, column=0, rowspan=7, padx=5, pady=5)

# Right column - Labels and Entry fields

frame_title = tk.Frame(root, bg="#303030")
frame_title.grid(row=0, column=1, padx=25, pady=5, sticky="ew")
title_label = tk.Label(frame_title, text="Startup Profit Predictor", font=("Times New Roman", 18), bg="#303030", fg="white")
title_label.pack()


# Frame for R&D Spend
frame_rd = tk.Frame(root, bg="#303030")
frame_rd.grid(row=1, column=1, padx=25, pady=5, sticky="ew")
rd_label = tk.Label(frame_rd, text="USD ($) spend on R&D:", font=("Times New Roman", 14), bg="#303030", fg="white")
rd_label.pack(side="left")
rd_spend = tk.Entry(frame_rd, font=("Times New Roman", 14), bg="#303030", fg="white")
rd_spend.pack(side="right")

# Frame for Administration
frame_admin = tk.Frame(root, bg="#303030")
frame_admin.grid(row=2, column=1, padx=25, pady=5, sticky="ew")
admin_label = tk.Label(frame_admin, text="USD ($) spend on Administration:", font=("Times New Roman", 14), bg="#303030", fg="white")
admin_label.pack(side="left")
admin = tk.Entry(frame_admin, font=("Times New Roman", 14), bg="#303030", fg="white")
admin.pack(side="right")

# Frame for Marketing Spend
frame_marketing = tk.Frame(root, bg="#303030")
frame_marketing.grid(row=3, column=1, padx=25, pady=5, sticky="ew")
marketing_label = tk.Label(frame_marketing, text="USD ($) spend on Marketing:", font=("Times New Roman", 14), bg="#303030", fg="white")
marketing_label.pack(side="left")
marketing = tk.Entry(frame_marketing, font=("Times New Roman", 14), bg="#303030", fg="white")
marketing.pack(side="right")

# Frame for State selection
frame_state = tk.Frame(root, bg="#303030")
frame_state.grid(row=4, column=1, padx=25, pady=5, sticky="ew")
state_label = tk.Label(frame_state, text="State (location of startup):", font=("Times New Roman", 14), bg="#303030", fg="white")
state_label.pack(side="left")
state = tk.StringVar()
state.set("California")
radio1 = tk.Radiobutton(frame_state, text="California", variable=state, value="California", font=("Times New Roman", 14), bg="#303030", fg="white")
radio1.pack(side="left")
radio2 = tk.Radiobutton(frame_state, text="Florida", variable=state, value="Florida", font=("Times New Roman", 14), bg="#303030", fg="white")
radio2.pack(side="left")
radio3 = tk.Radiobutton(frame_state, text="New York", variable=state, value="New York", font=("Times New Roman", 14), bg="#303030", fg="white")
radio3.pack(side="left")

# Predict button
button = tk.Button(root, text="Predict", command=predict, font=("Times New Roman", 16), bg="#4CAF50", fg="white")
button.grid(row=5, column=1, padx=30, pady=5, sticky="ew")

# Set background color
root.configure(bg="#303030")  # Dark gray background

root.mainloop()

