import rospy
from subprocess import Popen, PIPE, call
from std_msgs.msg import String

def callback(data):
  command = str(data.data)
  print "## effector_actions = " + command
  print "---"
  if not is_node_running(command):
    kill_node(command)
  if command == 'ig':
    call(['python','/home/ej/GIT/instructiongraphs/IGinterpreter/main.py','/home/ej/GIT/instructiongraphs/IGinterpreter/new.ig'])
  elif command == 'ig2':
    call(['python','/home/ej/GIT/instructiongraphs/IGinterpreter/main.py','/home/ej/GIT/instructiongraphs/IGinterpreter/new2.ig'])
  else:
    print 'I dont recongize this command'

def is_node_running(nodeName):
  p = Popen(['rosnode','info',nodeName], stdin=PIPE, stdout=PIPE)
  p2 = Popen(['grep','unknown node'], stdin=p.stdout, stdout=PIPE)
  p.stdout.close()
  output = p2.communicate()[0]
  p2.stdout.close()
  print ">>" + str(output)
  if str(output) == '':
    return True
  else:
    return False

def kill_node(nodeName):
  p = Popen(['rosnode','kill',nodeName], stdin=PIPE, stdout=PIPE)
  p.stdout.close()

def subscriber():
  rospy.init_node('effector', anonymous=False)
  rospy.Subscriber("effector_actions", String, callback)
  rospy.spin()

if __name__ == '__main__':
  try:
    # "/home/ej/GIT/instructiongraphs/IGinterpreter"
    call(["pwd"])
    subscriber()
  except rospy.ROSInterruptException:
    print 'Something went wrong!'



