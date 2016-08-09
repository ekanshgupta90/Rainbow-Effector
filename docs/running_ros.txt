# Rainbow Effector (rainbow_effector)

### Start ROS
```
roslaunch turtlebot_bringup minimal.launch
```

### Start navigation stack
```
roslaunch turtlebot_navigation amcl_demo.launch
```

### Start RViz for visualization
```
roslaunch turtlebot_rviz_launchers view_navigation.launch --screen
```

### Disable recovery behaviour
```
rosrun dynamic_reconfigure dynparam set /move_base recovery_behavior_enabled False

rosrun dynamic_reconfigure dynparam set /move_base clearing_rotation_allowed False

rosrun dynamic_reconfigure dynparam set /move_base shutdown_costmaps True
```

### Run the monitor
```
python monitor.py
```

Alternately, running through effector package
```
rospy <effector-package-name> monitor.py
```

### Run the effector
```
python effector.py
```

Alternately, running through effector package
```
rospy <effector-package-name> effector.py
```

### Run first instruction graph
To run first instruction graph from Instruction graph directory run:
```
python main.py <ig name>
```

Alternately, running through effector package
```
rospy <instruction-graph-package-name> main.py <ig-full-path>
```

### Adding obstacles on runtime
```
rosrun gazebo_ros spawn_model -file ~/.gazebo/models/cube_20k/model.sdf -sdf -model desk2 -x 5 -z 1
```

### Optional: To switch instruction graphs without obstacles
command.py script provides you an easy way to test effectors without using monitor.
```
python command.py
```

Alternately, running through effector package
```
rospy <effector-package-name> command.py
```


