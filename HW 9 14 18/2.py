import sys
if float(sys.argv[1]) < float(sys.argv[2]) < float(sys.argv[3]) or float(sys.argv[3]) < float(sys.argv[2]) < float(sys.argv[1]):
	print("True")
else:
	print("False")