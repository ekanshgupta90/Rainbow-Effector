# Simple monitor script.
# Subscribes to move_base status topic.
# On status = 4 triggers, ig swap on effector_actions topic.

import rospy
from std_msgs.msg import String
from actionlib_msgs.msg import GoalStatusArray
from actionlib_msgs.msg import GoalStatus

def init():
  rospy.init_node('monitor', anonymous=False)
  while rospy.get_time() == 0:
    pass
  

def subscribe():
  rospy.Subscriber("/move_base/status", GoalStatusArray, callback)
  rospy.spin()

def callback(goalStatusArray):
  pub = rospy.Publisher('effector_actions',String, queue_size=10)
  first = False
  for status in goalStatusArray.status_list:
    # status 4 in move base refers to obstacle/failed goal. 
    if int(status.status) == 4:
      rospy.loginfo("Encountered error switching IG")
      if not first:
        # Publishes a string value on the topic.
        pub.publish("ig2")
        first = True

if __name__ == '__main__':
  try:  
    init()
    subscribe()
  except rospy.ROSInterruptException:
    print "**Something went wrong!"