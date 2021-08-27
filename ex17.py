


#print("Copying from %s to %s" % (from_file, to_file))

from sys import argv; from os.path import exists; script, from_file, to_file = argv; in_file = open(from_file); indata = in_file.read(); out_file = open(to_file, "w"); out_file.write(indata); out_file.close(); in_file.close()


#print("the input file is %d bytes long" % len(indata))

#print("does the output file exist? %r" % exists(to_file))
#print("ready, hit RETURN to continue, CTRL-C to abort.")
#input()


#print("Alright, all done.")

# 6. because only can only open 500 files at once