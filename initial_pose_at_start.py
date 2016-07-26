import rospy
from geometry_msgs.msg import Point, Pose, PoseWithCovarianceStamped, Quaternion, Twist

def set_initial_pose(x, y):
  if not SETUP_DONE: setup()
  pub = rospy.Publisher('initialpose', PoseWithCovarianceStamped, queue_size=10, latch=True)

  initial_pose = PoseWithCovarianceStamped()

  initial_pose.header.stamp = rospy.Time.now()
  initial_pose.header.frame_id = 'map'

  initial_pose.pose.pose.position.x = 3.01
  initial_pose.pose.pose.position.y = 1.89
  initial_pose.pose.pose.position.z = 0
  initial_pose.pose.pose.orientation.x = 0
  initial_pose.pose.pose.orientation.y = 0
  initial_pose.pose.pose.orientation.z = 1
  initial_pose.pose.pose.orientation.w = 0
  initial_pose.pose.covariance = [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]

  pub.publish(initial_pose)

  time.sleep(1)

  if __name__ == '__main__':
    set_initial_pose(1,1);
