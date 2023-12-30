import tkinter as tk

# Создание главного окна приложения
app = tk.Tk()
app.title("Clicker Game")
app.geometry('400x200')


# Функция для увеличения счетчика
def counter():
    global count
    
    if count < 100:
        count += 1
    else:
        count += multiply
    
    label_counter["text"] = "На кнопку нажали: " + str(count) + " раз"
    
    if count >= 100 and not extra_button_shown:
        show_extra_button()


# Функция для увеличения множителя
def multiplier():
    global multiply
    
    multiply *= 2
    but_extra["text"] = "Нажми для +" + str(multiply) + " (достигнуто 100)"


# Функция для показа дополнительной кнопки
def show_extra_button():
    global extra_button_shown
    
    but_extra.pack(pady=10)
    extra_button_shown = True

count = 0
multiply = 2
extra_button_shown = False

label_counter = tk.Label(app, text="На кнопку еще никто не нажимал", font=("Arial", 16))
label_counter.pack(pady=20)

but_click = tk.Button(app, text="Click Me", width=10, height=2, command=counter)
but_click.pack(pady=10)

but_extra = tk.Button(app, text="Нажми для +" + str(multiply) + " (достигнуто 100)", width=30, height=2, command=multiplier)

app.mainloop()