from joblib import load
import tkinter

loaded_model = load('./model.pkl')

def predict(data):
    return loaded_model.predict(data)

def main():
    root = tkinter.Tk()
    root.title("Predictor")
    root.geometry("400x400")

    label = tkinter.Label(root, text="Enter the data")
    label.pack()

    entry = tkinter.Entry(root)
    entry.pack()

    def on_click():
        data = [float(entry.get())]
        result = predict([data])
        label.config(text=f"Prediction: {result}")

    button = tkinter.Button(root, text="Predict", command=on_click)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()