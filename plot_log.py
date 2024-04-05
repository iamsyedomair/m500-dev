import csv
import matplotlib.pyplot as plt

# Specify the path to your CSV file
csv_file = 'log0000/run/mpa/imu1/data.csv'

# Initialize empty lists to store the data
timestamps = []
ax_data = []
ay_data = []
az_data = []
gx_data = []
gy_data = []
gz_data = []
temperature_data = []

# Read the CSV file and extract the data
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if present
    for row in csv_reader:
        timestamps.append(float(row[1]))  # Convert timestamp to float
        ax_data.append(float(row[2]))
        ay_data.append(float(row[3]))
        az_data.append(float(row[4]))
        gx_data.append(float(row[5]))
        gy_data.append(float(row[6]))
        gz_data.append(float(row[7]))
        temperature_data.append(float(row[8]))

# Create a figure and subplots
fig, axs = plt.subplots(4, 1, figsize=(10, 12), sharex=True)

# Plot accelerometer data
axs[0].plot(timestamps, ax_data, label='AX')
axs[0].plot(timestamps, ay_data, label='AY')
axs[0].plot(timestamps, az_data, label='AZ')
axs[0].set_ylabel('Acceleration (m/s^2)')
axs[0].legend()

# Plot gyroscope data
axs[1].plot(timestamps, gx_data, label='GX')
axs[1].plot(timestamps, gy_data, label='GY')
axs[1].plot(timestamps, gz_data, label='GZ')
axs[1].set_ylabel('Angular Velocity (rad/s)')
axs[1].legend()

# Plot temperature data
axs[2].plot(timestamps, temperature_data, label='Temperature')
axs[2].set_ylabel('Temperature (°C)')
axs[2].legend()

# Set the x-axis label for the last subplot
axs[3].set_xlabel('Timestamp (ns)')

# Adjust the spacing between subplots
plt.tight_layout()

# Display the plot
plt.show()
