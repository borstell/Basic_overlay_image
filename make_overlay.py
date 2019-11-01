import os,sys

def make_overlay(lst):
	# Makes an overlay image
	a,b = lst.split(",")
	new_im = a.split(".")[0]+"_overlay."+a.split(".")[-1]
	img1 = a
	img2 = b
	string = "convert %s %s -alpha set \
					-compose dissolve -define compose:args='25' \
					-gravity Center -composite %s" % (img2, img1, new_im)
	os.system(string)

def main():
	make_overlay(sys.argv[1])

if __name__=="__main__":
	main()
