# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def count_words(content):
    count=0
    list=content.split()
    for count in range(1,len(list)):
        count=count+1
    return count

passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print count_words(passage)
#>>>56








# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000. # km per second

def speed_fraction(traceroute,distance):
    speed=float(2*distance)/float(traceroute)
    return speed*1000/float(speed_of_light)




print speed_fraction(50,5000)
#>>> 0.666666666667

print speed_fraction(50,10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?








# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(time):
    h=int(time)/3600
    m=(int(time)-h*3600)/60
    s=time-h*3600-m*60
    if h==1:nh='hour'
    else:nh='hours'
    if m==1:nm='minute'
    else:nm='minutes'
    if s==1:ns='second'
    else:ns='seconds'
    return '%s %s, %s %s, %s %s' %(h,nh,m,nm,s,ns)

print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds











# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def convert_seconds(time):
    h=int(time)/3600
    m=(int(time)-h*3600)/60
    s=time-h*3600-m*60
    if h==1:nh='hour'
    else:nh='hours'
    if m==1:nm='minute'
    else:nm='minutes'
    if s==1:ns='second'
    else:ns='seconds'
    return '%s %s, %s %s, %s %s' %(h,nh,m,nm,s,ns)


def download_time(fsize,funit,bw,bwunit):
    if funit[1]=='B':
        if funit[0]=='k':
            fsize=float(fsize*(2**10)*8)
        if funit[0]=='M':
            fsize=float(fsize*(2**20)*8)
        if funit[0]=='G':
            fsize=float(fsize*(2**30)*8)
        if funit[0]=='T':
            fsize=float(fsize*(2**40)*8)
    if funit[1]=='b':
        if funit[0]=='k':
            fsize=float(fsize*2**10)
        if funit[0]=='M':
            fsize=float(fsize*2**20)
        if funit[0]=='G':
            fsize=float(fsize*2**30)
        if funit[0]=='T':
            fsize=float(fsize*2**40)
    if bwunit[1]=='B':
        if bwunit[0]=='k':
            bw=bw*(2**10)*8
        if bwunit[0]=='M':
            bw=bw*(2**20)*8
        if bwunit[0]=='G':
            bw=bw*(2**30)*8
        if bwunit[0]=='T':
            bw=bw*(2**40)*8
    if bwunit[1]=='b':
        if bwunit[0]=='k':
            bw=bw*2**10
        if bwunit[0]=='M':
            bw=bw*2**20
        if bwunit[0]=='G':
            bw=bw*2**30
        if bwunit[0]=='T':
            bw=bw*2**40
    total_time=fsize/bw
    return convert_seconds(total_time)


print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable






#example from the forum

def download_time(file_size, file_units, bandwidth, band_units):
    units = ["kb", "kB", "Mb", "MB", "Gb", "GB", "Tb", "TB"]
    size_value = [2**10, 2**10*8, 2**20, 2**20*8, 
                  2**30, 2**30*8, 2**40, 2**40*8]
    
    total_time = (file_size * size_value[units.index(file_units)]) / (bandwidth * size_value[units.index(band_units)])
    hours = int(total_time / 3600)
    minutes = int(total_time % 3600) / 60
    seconds = (float(total_time) % 3600) % 60
    
    return str(hours) + (" hour, ", " hours, ")[hours != 1] + \
           str(minutes) + (" minute, ", " minutes, ")[minutes != 1] + \
           str(seconds) + (" second ", " seconds ")[seconds != 1]
