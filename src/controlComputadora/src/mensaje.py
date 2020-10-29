#! /usr/bin/env python

import rospy
from std_msgs.msg import String

def NodoMamoncito():
	print ("Dame tu movimiento")

	#movimiento = input()

	movimiento = raw_input()
	print (movimiento)

	pub = rospy.Publisher('aqui_va_el_topico',String,queue_size=10)
 
	#rospy.init_node('NodoMamoncito', anonymus = True)
	rospy.init_node('NodoMamoncito')
	print "Nodo creado con exito"


	rate = rospy.Rate(1) #frecuencia con la que va atrabajar el nodo
	while not rospy.is_shutdown():
		hello = "tiempo transcurrido %s" % rospy.get_time()
		pub.publish(movimiento)
		print ("se logro")
		rate.sleep()

if __name__ == '__main__':
	try:
		NodoMamoncito()
	except rospy.ROSInterruptException:
		pass



	

	
 
