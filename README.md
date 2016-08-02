# Rainbow Effector (rainbow_effector)

## Running effector

### Start ROS
```
roslaunch turtlebot_bringup minimal.launch
```

### (Optional) Start navigation stack
```
roslaunch turtlebot_navigation amcl_demo.launch
```

### (Optional) Start RViz for visualization
```
roslaunch turtlebot_rviz_launchers view_navigation.launch --screen
```

### Disable recovery behaviour
```
rosrun dynamic_reconfigure dynparam set /move_base recovery_behavior_enabled False

rosrun dynamic_reconfigure dynparam set /move_base clearing_rotation_allowed False

rosrun dynamic_reconfigure dynparam set /move_base shutdown_costmaps True
```

### Run the effector
```
python command.py
```


### Adding obstacles on runtime
```
rosrun gazebo_ros spawn_model -file ~/.gazebo/models/cube_20k/model.sdf -sdf -model desk2 -x 5 -z 1
```
