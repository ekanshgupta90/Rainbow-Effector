import rospy
from std_msgs.msg import String

def publisher():
  pub = rospy.Publisher('effector_actions',String, queue_size=10)
  rospy.init_node('effector_sim', anonymous=False)
  
  while not rospy.is_shutdown():
    print "\n==Options== \n 1. Autonomous nav \n 2. IG"
    input = raw_input('Select a value:')
    try:
      if int(input) == 1:
        print ">>Publishing auto_nav to effector_actions"
        pub.publish("auto_nav")
      elif int(input) == 2:
        print ">>Publishing ig to effector_actions"
        pub.publish("ig")
      else:
        print "**Please select a value from the options above"
    except ValueError:
      print "**Value should be numeric"

if __name__ == '__main__':
  try:  
    publisher()
  except rospy.ROSInterruptException:
    print "**Something went wrong!"
      


