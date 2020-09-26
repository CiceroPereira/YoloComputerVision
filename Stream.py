import cv2
import sys
from threading import Thread
from queue import Queue 


class Stream:
	def __init__(self, path, queueSize = 128):

		self.stream = cv2.VideoCapture(path)
		self.isStopped = False
		self.queue = Queue(maxsize=queueSize)
		self.start()


	def start(self):

		t = Thread(target= self.update)
		t.setDaemon(True)
		t.start()
		return self


	def update(self):

		while(True):
			

			if self.isStopped:
				return

			if not self.queue.full():
				
				ret, frame = self.stream.read()
				

				if not ret:
					self.stop()
	
				
				self.queue.put(frame) 


	def read(self):
		return self.queue.get()


	def isRunning(self):
		return self.queue.qsize() > 0


	def stop(self):
		self.isStopped = True