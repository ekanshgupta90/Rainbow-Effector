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
    if int(status.status) == 4:
      rospy.loginfo("Encountered error switching IG")
      if not first:
        pub.publish("ig2")
        first = True

if __name__ == '__main__':
  try:  
    init()
    subscribe()
  except rospy.ROSInterruptException:
    print "**Something went wrong!"