# m500-dev


voxl-logger -i imu1 -s 5000 --note "primary imu test"

To log one camera image:

```yocto:/# voxl-logger --cam tracking --samples 1```
To log 5000 imu samples:

```yocto:/# voxl-logger -i imu1 -s 5000 --note "primary imu test"```
To log 1000 imu0 samples and 2000 imu1 samples:

```yocto:/# voxl-logger -i imu0 -s 1000 -i imu1 -s 2000```
To log every 5th imu sample (skip 4) for 5.5 seconds:

```yocto:/# voxl-logger -i imu1 --skip 4 -t 5.5```
To log tracking camera and both imus until you press ctrl-c

```yocto:/# voxl-logger --preset_odometry```
To record a typical log for testing VIO (imu + tracking) for 1 minute

```yocto:/# voxl-logger --preset_odometry --time 60 --note "log for vio replay test 1"```

