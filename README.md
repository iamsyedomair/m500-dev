## To log one camera image:
voxl-logger --cam tracking --samples 1

### To log 5000 imu samples:
voxl-logger -i imu1 -s 5000 --note "primary imu test"

### To log 1000 imu0 samples and 2000 imu1 samples:
voxl-logger -i imu0 -s 1000 -i imu1 -s 2000

### To log every 5th imu sample (skip 4) for 5.5 seconds:
voxl-logger -i imu1 --skip 4 -t 5.5

### To log tracking camera and both imus until you press ctrl-c
voxl-logger --preset_odometry

### To record a typical log for testing VIO (imu + tracking) for 1 minute
voxl-logger --preset_odometry --time 60 --note "log for vio replay test 1"


[notion link for more details on the hardware setup](https://www.notion.so/agrawala96/Modal-AI-Flight-1e54ca92fe014b9abe38a9c0fd772a30)
