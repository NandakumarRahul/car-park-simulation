from tkinter import *
import CarPark as ck
carpark = ck.CarPark(6)
def entry():
    def call():
        temp = vehicle_id.get()
        vehicle_i,space_id,entry_time,available_spaces= carpark.enter(temp)
        result = Label(window, text = "")
        result.pack()
        result.config(text = f"Vehicle {vehicle_i} has entered the car park \n Parking space ID: {space_id} \n Entry time : {entry_time}\nRemaining available space : {available_spaces}")
    label = Label(window,text='Enter vehicle ID : ',font=('Arial',10),bd=10)
    label.pack()
    vehicle_id = StringVar()
    entry = Entry(window, textvariable = vehicle_id, font=('Arial',10),bd=10)
    entry.pack()
    submit_button = Button(window, text='Enter the car park', font=('Arial', 10), fg='Blue',width=15, command= call)
    submit_button.pack()
def exit():
    def call():
        temp = vehicle_id.get()
        vehicle_i, space_id,entry_time,exit_time,fare,available_spaces=carpark.exit(temp)
        result = Label(window, text = "")
        result.pack()
        result.config(text = f"Vehicle {vehicle_i} has exited the car park.\nParking space ID:{space_id}\nEntry time :{entry_time}\nExit time : {exit_time} \nFare: £{fare}\nRemaining available space : {available_spaces}")
    label = Label(window,text='Enter vehicle ID : ',font=('Arial',10),bd=10)
    label.pack()
    vehicle_id = StringVar()
    entry = Entry(window, textvariable = vehicle_id, font=('Arial',10),bd=10)
    entry.pack()
    submit_button = Button(window, text='Exit the car park', font=('Arial', 10), fg='Blue',width=15,command= call)
    submit_button.pack()
def enquire():
    def call():
        temp = vehicle_id.get()
        vehicle_i, space_id, entry_time=carpark.enquire(temp)
        result = Label(window, text = "")
        result.config(text=f"Vehicle {vehicle_id} is parked in space ID {space_id} \nEntry time : {entry_time}")
        result.pack()
        result.config()
    label = Label(window,text='Enter vehicle ID : ',font=('Arial',10),bd=10)
    label.pack()
    vehicle_id = StringVar()
    entry = Entry(window, textvariable = vehicle_id, font=('Arial',10),bd=10)
    entry.pack()
    submit_button = Button(window, text='Enquire', font=('Arial', 10), fg='Blue',width=15,command= call)
    submit_button.pack()
def kill():
    window.destroy()
window = Tk()

button_1 = Button(window,text='Enter the car park',font=('Arial',10),fg='Blue',width=20,command=entry)
button_1.pack()
button_2 = Button(window,text='Exit the car park',font=('Arial',10),fg='Blue',width=20,command=exit)
button_2.pack()
button_3 = Button(window,text='Enquiry',font=('Arial',10),fg='Blue',width=20,command=enquire)
button_3.pack()
button_4 = Button(window,text='Quit',font=('Arial',10),fg='Blue',width=20, command=kill)
button_4.pack()


window.geometry('420x420')
window.title("CAR PARKING SIMULATOR")
window.mainloop()