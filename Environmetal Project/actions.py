import matplotlib.pyplot as plt  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

current_canvas = None

def show_city_graph(city_name, parent_window):
    global current_canvas
    
    
    if current_canvas is not None:
        current_canvas.get_tk_widget().destroy()
        current_canvas = None
    
    
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    pollution = {
        "Austin": [15, 14.8, 14.6, 14.4, 14, 13.6, 13.3, 12.9, 12.5, 12, 11.5, 9.6, 9.3, 9.0, 8.7],
        "Dallas": [17.2, 16.9, 16.6, 16.3, 16, 14.7, 14.4, 14.1, 13.8, 13.5, 13.2, 12.9, 12.6, 12.3, 12],
        "Houston": [35, 34.8, 34.6, 34.4, 33.4, 33, 32.5, 32, 31.5, 31, 30.05, 29.7, 29.3, 29, 28.7]
    }

    
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(years, pollution[city_name], marker='o', color='blue')
    ax.set_title(f"{city_name} CO2 Pollution Since 2010")
    ax.set_xlabel("Year")
    ax.set_ylabel("Carbon Dioxide (Million Metric Tons)")

    
    current_canvas = FigureCanvasTkAgg(fig, master=parent_window)
    current_canvas.draw()
    current_canvas.get_tk_widget().pack(pady=10)