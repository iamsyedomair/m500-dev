from pymavlink import mavutil
import time

# Connect to the drone
drone = mavutil.mavlink_connection("udpin:localhost:14445")

# Wait for the first heartbeat
drone.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (drone.target_system, drone.target_component))

# Request the ATTITUDE_QUATERNION message at 5 Hz
drone.mav.request_data_stream_send(drone.target_system, drone.target_component, mavutil.mavlink.MAV_DATA_STREAM_EXTRA1, 5, 1)

# Continuously read messages
while True:
    msg = drone.recv_match(type='ATTITUDE_QUATERNION', blocking=True)
    if msg:
        print("Attitude Quaternion:")
        print("  q1: %f" % msg.q1)
        print("  q2: %f" % msg.q2)
        print("  q3: %f" % msg.q3)
        print("  q4: %f" % msg.q4)
        print("  rollspeed: %f" % msg.rollspeed)
        print("  pitchspeed: %f" % msg.pitchspeed)
        print("  yawspeed: %f" % msg.yawspeed)
        print("  time_boot_ms: %d" % msg.time_boot_ms)
        print("------------------------")
        
        # Sleep for a short duration to control the reading rate
        time.sleep(0.2)  # Read at approximately 5 times per second
