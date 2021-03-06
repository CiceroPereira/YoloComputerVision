import cv2
import numpy as np

class Detections:

	def yolo(self, image):
		
		#file_name = "Images/knife_" + str(image_index) + ".txt"	
		weights = "Weights/yolov4-obj_final.weights"
		config = "Config/yolov4-obj.cfg"

		net = cv2.dnn.readNetFromDarknet(config, weights)
		#net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
		#net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

		classes = []
		with open("Config/obj.names","r") as f:
		    classes = [line.strip() for line in f.readlines()]

		layer_names = net.getLayerNames()
		outputlayers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]    

		colors= np.random.uniform(0,255,size=(len(classes),3))

		img = image
		height,width,channels = img.shape

		blob = cv2.dnn.blobFromImage(img,0.00392,(416,416),(0,0,0),True,crop=False)


		# for b in blob:
		#     for n,img_blob in enumerate(b):
		#         cv2.imshow(str(n),img_blob)
		        
		net.setInput(blob)
		outs = net.forward(outputlayers)


		class_ids=[]
		confidences=[]
		boxes=[]
		centers=[]
		for out in outs:
		    for detection in out:
		        scores = detection[5:]
		        class_id = np.argmax(scores)
		        confidence = scores[class_id]
		        if confidence > 0.5:
		            
		            center_x= int(detection[0]*width)
		            center_y= int(detection[1]*height)
		            w = int(detection[2]*width)
		            h = int(detection[3]*height)
		        
		            x=int(center_x - w/2)
		            y=int(center_y - h/2)

		            
		            centers.append([center_x, center_y])
		            boxes.append([x,y,w,h])
		            confidences.append(float(confidence)) 
		            class_ids.append(class_id) 
		        
					
		indexes = cv2.dnn.NMSBoxes(boxes,confidences,0.4,0.6)


		font = cv2.FONT_HERSHEY_PLAIN
		for i in range(len(boxes)):
		    if i in indexes:
		        x,y,w,h = boxes[i]
		        center_x, center_y = centers[i]
		        label = str(classes[class_ids[i]])
		        color = colors[int(class_ids[i])]
		        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
		        cv2.putText(img,label + ': ' + str(confidences[i]),(x,y+30),font,1,(0,255,255),2)
		   #     f = open(file_name, "a")
		    #    string = str(class_ids[i]) + " " + str(center_x/width)  + " " + str(center_y/height)  + " " + str(w/width)  + " " + str(h/height) + "\n"
		     #   f.write(string)
		        f.close()		       

		return img;