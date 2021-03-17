#!/usr/bin/env python
import sys, rospy
from mymouse_ros.msg import MyLightSensorValues

if __name__ == '__main__':
    devfile = '/dev/rtlightsensor0'
    rospy.init_node('lightsensors')
    pub = rospy.Publisher('lightsensors',MyLightSensorValues, queue_size=1)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            with open(devfile,'r') as f:
                data = f.readline().split()
		data = [ int(e) for e in data ]
		d = MyLightSensorValues()
		d.left_third = data[0]
                d.left_first = data[1]
                d.right_first = data[2]
		d.right_third = data[3]
		d.left_second = (data[0]+data[1])/2
                d.sentor = (data[1]+data[2])/2
		d.right_second = (data[2]+data[3])/2
                pub.publish(d)

	except I0Error:
	    rospy.logerr("cannot write to " + devfile)
	rate.sleep()
