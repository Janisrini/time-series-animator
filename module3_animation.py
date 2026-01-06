import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load cleaned data
df = pd.read_csv("cleaned_time_series.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))
line1, = ax.plot([], [], label='Temperature (°C)', color='red')
line2, = ax.plot([], [], label='Rainfall (mm)', color='blue')
line3, = ax.plot([], [], label='Humidity (%)', color='green')

ax.set_xlim(df['Date'].min(), df['Date'].max())
ax.set_ylim(0, max(df[['Temperature', 'Rainfall', 'Humidity']].max()) + 10)
ax.set_xlabel("Date")
ax.set_ylabel("Value")
ax.set_title("Time Series Animation")
ax.legend()
ax.grid(True)

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line1, line2, line3

def update(frame):
    x = df['Date'][:frame]
    y1 = df['Temperature'][:frame]
    y2 = df['Rainfall'][:frame]
    y3 = df['Humidity'][:frame]
    
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    line3.set_data(x, y3)
    
    return line1, line2, line3

ani = animation.FuncAnimation(fig, update, frames=len(df),
                              init_func=init, blit=True, interval=200)

plt.tight_layout()
plt.show()

# To save the animation as a gif:
# ani.save("time_series_animation.gif", writer="pillow")