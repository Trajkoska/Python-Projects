import requests
import tkinter as tk
from datetime import datetime, timedelta
from PIL import Image, ImageTk
import io
from tkinter import messagebox


def clear_indicating_text(event):
    if enterlocation.get() == indicating_text:
        enterlocation.delete(0, tk.END)
        enterlocation.config(fg='black')

def restore_indicating_text(event):
    if not enterlocation.get():
        enterlocation.insert(0, indicating_text)
        enterlocation.config(fg='gray')

def handle_click(event):
    if event.widget != indicating_text and enterlocation.get() == "":
        enterlocation.delete(0, tk.END)
        enterlocation.insert(0, indicating_text)
        enterlocation.config(fg='gray')
        enterlocation.icursor(0)  
    else:
        if enterlocation.get() == indicating_text:
            enterlocation.delete(0, tk.END)
            enterlocation.icursor(0)
        enterlocation.bind('<Key>', clear_on_typing)

def clear_on_typing(event):
    enterlocation.unbind('<Key>')
    enterlocation.config(fg='black')

screen = tk.Tk()
screen.geometry("1600x1000")
screen.title("Weather App")

indicating_text = "Enter location..."

C = tk.Canvas(screen, bg="blue", height=700, width=500)
filename = tk.PhotoImage(file = "background.png")
background_label = tk.Label(screen, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.create_text(1000,1000, text="Welcome to WeatherAPI", fill="white", font="Helvetica 40") ## ne se pokazuva


enterlocation = tk.Entry(screen,font="Helvetica 14",fg='gray')
enterlocation.insert(0, indicating_text)
enterlocation.config(fg='gray')  # Set text color to gray
enterlocation.bind('<FocusIn>', clear_indicating_text)
enterlocation.bind('<FocusOut>', restore_indicating_text)
enterlocation.grid(column=5, row=4, padx=(650, 10), pady=30)


def search():
    try:
        location = enterlocation.get()
        url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

        querystring = {"q": location, "days": "3"}

        headers = {
            "X-RapidAPI-Key": "725a212234mshfc3c90a2ee9d5c1p1a47acjsn4c6f556d6eef",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        country = data['location']['country']
        local_time = data['location']['localtime']
        last_updated = data['current']['last_updated']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        wind_kph = data['current']['wind_kph']
        humidity = data['current']['humidity']
        feels_like = data['current']['feelslike_c']

        photo_url = "https:" + data['current']['condition']['icon']

        image_response = requests.get(photo_url)
        image_data = Image.open(io.BytesIO(image_response.content))

        photo_image = ImageTk.PhotoImage(image_data)

        forecast_data = data['forecast']['forecastday'][1:3]

        api_info_label = tk.Label(screen, text="", justify="left", bg="#4D99E7", fg="black", font=("Helvetica", 15),
                                  anchor="w", padx=10)
        api_info_label.grid(column=5, row=7, columnspan=1)

        api2_info_label = tk.Label(screen, text="", justify="left", anchor="w", font=("Helvetica", 42), bg="#4D99E7")
        api2_info_label.grid(column=5, row=6, padx=(600, 0), columnspan=2, pady=20)

        api3_info_label = tk.Label(screen, text="", justify="left", anchor="w", padx=10, font=30, bg="#B1D2F1")
        api3_info_label.grid(column=6, row=7, columnspan=5)

        # Create Label widget for displaying the PNG photo
        api_photo_label = tk.Label(screen)

        api_photo_label.grid(column=6, row=6, pady=50)

        api_info_label.config(
            text=f"Country: {country}\nLocal Time: {local_time}\nLast Updated: {last_updated}\n"
                 f"Condition: {condition}\nWind Speed: {wind_kph} km/h\n"
                 f"Humidity: {humidity}%\nFeels Like: {feels_like}°C\n"
        )
        api2_info_label.config(text=f"{temp_c}°C")
        api3_info_label.config(text=f"Forecast for the next two days:\n\n"
                                    f"Date: {forecast_data[0]['date']}\nMax Temperature: {forecast_data[0]['day']['maxtemp_c']}°C\n"
                                    f"Min Temperature: {forecast_data[0]['day']['mintemp_c']}°C\n\n"
                                    f"Date: {forecast_data[1]['date']}\nMax Temperature: {forecast_data[1]['day']['maxtemp_c']}°C\n"
                                    f"Min Temperature: {forecast_data[1]['day']['mintemp_c']}°C\n")

        api_photo_label.config(image=photo_image)
        api_photo_label.image = photo_image
    except:
        messagebox.showerror("Error","The city you inserted doesn't exist.")



search_location_button = tk.Button(text="Search", command=search)
search_location_button.grid(column=6, row=4,)

screen.bind('<Button-1>', lambda event, screen=screen: handle_click(event))


screen.mainloop()
