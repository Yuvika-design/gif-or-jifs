import imageio.v3 as io
img_location=["1.jpg","2.jpg","3.jpg","4.jpg"] #locations of the images stored in this list
images=[] #this list will store the images
for i in img_location:
	images.append(io.imread(i))
	#imread() loads an img based on its filepath
	io.imwrite("clock.gif",images,duration=0.5,loop=0)#.imwrite()method used to turn images into gifs


