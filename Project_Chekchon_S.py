from tkinter import *
import tkinter as tk

class PercentConvert:
    def convert(self):

        #รับค่าราคาและเปอร์เซ็นต์
        price = float(self.price_entry.get())
        percent = float(self.percent_entry.get())

        #คำนวณราคาที่ลด
        discount = price * (percent/100)
        self.discount_entry.delete(0, tk.END)
        self.discount_entry.insert(0, discount)

        #คำนวณราคาที่ต้องจ่าย
        totalprice = price - discount
        self.totalprice_entry.delete(0, tk.END)
        self.totalprice_entry.insert(0, totalprice)

    #ส่วนหน้าตาของโปรมแกรม
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Percent Convert")
        self.window.geometry("400x200")

        self.price_label = tk.Label(self.window, text = " Price (Baht) ")
        self.price_label.grid(row=0, column=0)
        self.percent_label = tk.Label(self.window, text = " Percent (%) ")
        self.percent_label.grid(row=1 , column=0)
        self.discount_label = tk.Label(self.window, text = " Discount (Baht) ")
        self.discount_label.grid(row=2 ,column=0)
        self.totalprice_label = tk.Label(self.window, text = " Total Price (Baht) ")
        self.totalprice_label.grid(row=3 ,column=0)
        self.price_entry = tk.Entry(self.window)
        self.price_entry.grid(row=0, column=1)
        self.percent_entry = tk.Entry(self.window)
        self.percent_entry.grid(row=1, column=1)
        self.discount_entry = tk.Entry(self.window)
        self.discount_entry.grid(row=2, column=1)
        self.totalprice_entry = tk.Entry(self.window)
        self.totalprice_entry.grid(row=3, column=1)

        self.button_convert = tk.Button(self.window, text = "convert", command = self.convert)
        self.button_convert.grid(row=4 , column=1)

        self.button_reset = tk.Button(self.window, text="reset", command=self.reset)
        self.button_reset.grid(row=5, column=3)

        self.window.mainloop()

    def reset(self):
        self.price_entry.delete(0, tk.END)
        self.percent_entry.delete(0,tk.END)
        self.discount_entry.delete(0,tk.END)
        self.totalprice_entry.delete(0,tk.END)

app = PercentConvert()


