import json
from selenium import webdriver
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from CTkMessagebox import CTkMessagebox
import os
USERNAME = ""
USERNAME_ = ""


def main():
    global USERNAME, USERNAME_

    def make_transaction():
        accountt = transaction_user_entry.get()
        amountt = transaction_am_entry.get()
        passwordd = transaction_pas_entry.get()
        global USERNAME_, USERNAME
        USERNAME_ = accountt
        with open("data.json", "r") as ddddd:
            data__ = json.load(ddddd)
            if accountt in data__.keys():
                if len(passwordd) == 0:
                    CTkMessagebox(title="Error", message="Please enter your password.", icon="warning", option_1="OK")
                if passwordd == data__[USERNAME]["password"]:
                    bal = data__[USERNAME]["balance"]
                    if int(amountt) <= int(bal):
                        new_balance = int(bal) - int(amountt)
                        data__[USERNAME]["balance"] = new_balance
                        bal2 = data__[USERNAME_]["balance"]
                        new_balance2 = int(bal2) + int(amountt)
                        data__[USERNAME_]["balance"] = new_balance2
                        with open("data.json", "w") as d_:
                            json.dump(data__, d_, indent=4)
                            balance_label.configure(text=f"Balance: {new_balance}")
                        CTkMessagebox(title="Done", message="Transaction made succesfully.", icon="check", option_1="OK")
                    else:
                        CTkMessagebox(title="Error", message="The amount you want to transfer is greater than your balance.", icon="cancel", option_1="OK")
                else:
                    CTkMessagebox(title="Error", message="Wrong password.", icon="cancel", option_1="OK")
            else:
                CTkMessagebox(title="Error", message="The account you entered does not exist in our database.",
                              icon="cancel", option_1="OK")


    def fund_money():
        money = money_entry.get()
        with open("data.json", "r") as d_:
            dat_ = json.load(d_)
            fund_amount = dat_[USERNAME]["balance"]
            fund = int(fund_amount) + int(money)
            dat_[USERNAME]["balance"] = fund
        with open("data.json", "w") as d_:
            json.dump(dat_, d_, indent=4)
        balance_label.configure(text = f"Balance: {fund}")

    def withdrawal_money():
        money = money_entry.get()
        with open("data.json", "r") as d_:
            dat_ = json.load(d_)
            fund_amount = dat_[USERNAME]["balance"]
            fund = int(fund_amount) - int(money)
            dat_[USERNAME]["balance"] = fund
        with open("data.json", "w") as d_:
            json.dump(dat_, d_, indent=4)
        balance_label.configure(text=f"Balance: {fund}")

    def change_pas():
        global USERNAME

        with open("data.json", "r") as d_:
            dat_ = json.load(d_)

        def change():
            

        old_pas_data = dat_[USERNAME]["password"]

        pas_window = ctk.CTk()
        pas_window.geometry("230x200")
        pas_window.title("Change password")
        ctk.set_appearance_mode("dark")

        old_pas = ctk.CTkEntry(pas_window, placeholder_text="Old password", width=300, corner_radius=10)
        old_pas.pack()

        repeat_pas = ctk.CTkEntry(pas_window, placeholder_text="Repeat old password", width=300, corner_radius=10)
        repeat_pas.pack()

        new_pas = ctk.CTkEntry(pas_window, placeholder_text="New password", width=300, corner_radius=10)
        new_pas.pack()

        conf_button = ctk.CTkButton(pas_window, text="Confirm", fg_color="gray", corner_radius=10, command = change)
        confirm_button.pack()





    main_window = ctk.CTk()
    main_window.geometry("800x400")
    main_window.title("Your bank account")
    ctk.set_appearance_mode("dark")

    usern_ = login_username_entry.get()
    global USERNAME

    with open("data.json", "r") as ddd:
        dataa = json.load(ddd)
        balans = dataa[USERNAME]["balance"]


    balance_label = ctk.CTkLabel(main_window, text=f"Balance: {balans}", anchor="center")
    balance_label.grid(row = 0, column = 0, padx = (150, 20), pady = (20,20))

    money_entry = ctk.CTkEntry(main_window, placeholder_text="Insert amount of money", width=250, corner_radius=10)
    money_entry.grid(row = 1, column = 0, columnspan = 2, padx = 10)

    withdrawal_button = ctk.CTkButton(main_window, text="Withdrawal", fg_color="gray", corner_radius=10, width=110, command=withdrawal_money)
    withdrawal_button.grid(row = 2, column = 0, padx = (0, 0))

    fund_button = ctk.CTkButton(main_window, text="Fund", fg_color="gray", corner_radius=10, width=110, compound="left", command=fund_money)
    fund_button.grid(row = 2, column = 1, padx = (0, 60))

    transaction_label = ctk.CTkLabel(main_window, text="Make a transaction")
    transaction_label.grid(row = 0, column = 2)

    transaction_user_entry = ctk.CTkEntry(main_window, placeholder_text="Insert account", width=300, corner_radius=10)
    transaction_user_entry.grid(row = 1, column = 2, pady= 3)

    transaction_am_entry = ctk.CTkEntry(main_window, placeholder_text="Insert amount", width=300, corner_radius=10)
    transaction_am_entry.grid(row = 2, column = 2,)

    transaction_pas_entry = ctk.CTkEntry(main_window, placeholder_text="Insert your password", width=300, corner_radius=10)
    transaction_pas_entry.grid(row = 3, column = 2, pady = 3)

    confirm_button = ctk.CTkButton(main_window, text="Confirm", fg_color="gray", corner_radius=10, compound="left", command=make_transaction)
    confirm_button.grid(row = 4, column = 2, pady = 5)

    change_pas_button = ctk.CTkButton(main_window, text="Change your password", fg_color="gray", corner_radius=10, width = 200)
    change_pas_button.grid(row = 5, column = 2, pady = (166,2), padx = (195, 2))




    main_window.mainloop()


def login1():
    passw = login_pas_entry.get()
    usern = login_username_entry.get()
    global USERNAME
    USERNAME = usern
    with open("data.json", "r") as dd:
        data_ = json.load(dd)
        if usern in data_.keys():
            if passw == data_[usern]["password"]:
                main()
            else:
                CTkMessagebox(title="Error", message="Wrong password.", icon="cancel", option_1="OK")
        else:
            CTkMessagebox(title="Error", message="The account you entered does not exist. Please register.", icon="cancel", option_1="OK")


def register():

    def save():
        password = reg_pas_entry.get()
        username = reg_username_entry.get()
        new_dict = {username:{"password": password, "balance":0}}
        with open("data.json", "r") as d:
            data = json.load(d)
            if data.get(username):
                CTkMessagebox(title="Sorry...", message="This username is already taken. Try another.", icon="cancel", option_1="OK")
            if len(password) == 0:
                CTkMessagebox(title="Error", message="Please insert a password.", icon="warning", option_1="OK")
            else:
                data.update(new_dict)
        with open("data.json", "w") as d:
            json.dump(data, d, indent=4)

    reg_window = ctk.CTk()
    reg_window.geometry("230x200")
    reg_window.title("Register")
    ctk.set_appearance_mode("dark")

    reg_username_entry = ctk.CTkEntry(reg_window, placeholder_text="Username", width=170, corner_radius=10, )
    reg_username_entry.pack(pady =(45,5))

    reg_pas_entry = ctk.CTkEntry(reg_window, placeholder_text="Password", width=170, corner_radius=10)
    reg_pas_entry.pack()

    confirm_button = ctk.CTkButton(reg_window, text="Confirm", fg_color="gray", corner_radius=10, command=save)
    confirm_button.pack(pady = 10)
    reg_window.mainloop()




image = ctk.CTkImage(light_image=Image.open("photo.png"), size=(180, 150))

window = ctk.CTk()
window.geometry("600x500")
window.title("Bank system")
ctk.set_appearance_mode("dark")


login = ctk.CTkLabel(window, text="", image=image)
login.pack()

login_label = ctk.CTkLabel(window, text="Login")
login_label.pack()

login_username_entry = ctk.CTkEntry(window, placeholder_text= "Username", width = 170, corner_radius=10)
login_username_entry.pack()

login_pas_entry = ctk.CTkEntry(window, placeholder_text= "Password", width = 170, corner_radius=10)
login_pas_entry.pack()

login_button = ctk.CTkButton(window, text = "Login", fg_color="gray", corner_radius=10, command=login1)
login_button.pack()

register_label = ctk.CTkLabel(window, text="Don't have account?")
register_label.pack()
register_button = ctk.CTkButton(window, text = "Register", fg_color="gray", corner_radius=10, command=register)
register_button.pack()

reset_label = ctk.CTkLabel(window, text="Forgot your password?")
reset_label.pack()
request_button = ctk.CTkButton(window, text = "Request new password", fg_color="gray", corner_radius=10)
request_button.pack()



window.mainloop()
