def fileread():
    try:
        myfile = open("F:\song.wav","r")
        data = myfile.read()
    except(IOError):
        print "Sorry file not found"       
    else:
        print data

def writemusic():
    try:
        myfile = open("F:\music.wav","w")
        data = "RIFF K[]"
        myfile.write(data)
    except(IOError):
        print "Sorry file not found"
    else:
        print "Write successful"
