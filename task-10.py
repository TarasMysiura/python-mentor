import tkinter as tk

# Создаем окно
my_calc = tk.Tk()

# Получаем ширину и высоту экрана
screen_width = my_calc.winfo_screenwidth()
screen_height = my_calc.winfo_screenheight()
print(screen_width, screen_height)

# Вычисляем координаты окна приложения
window_width = 500
window_height = 300
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
my_calc.geometry(f"{window_width}x{window_height}+{x}+{y}")
# my_calc.geometry(f"{500}x{300}+{x}+{y}")

# Запускаем программу
my_calc.mainloop()
