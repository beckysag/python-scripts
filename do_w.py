import sys
import subprocess
import shlex
import getopt

# This program accepts one optional command line argument  
# Uses subprocess.Popen() to connect to the Unix/Linux command "w" and one of the command line 
# arguments [-h, -u, -s, -f, -V], and prints the results from running them through Popen.

def main():
    pass

def do_w():
    # possible parameters
    allowed = ['-h', '-u', '-s', '-f', '-v']
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'husfV')
    except getopt.GetoptError, err:
        print str(err)
        sys.exit(1)                                                                                                                                         
        
    # Make sure no more than one parameter was entered
    if (len(opts) > 1):
        print "Only one command line option may be entered."
        sys.exit(1)
        
    elif ((len(opts) == 0)):
        opt = ''

    else:
        opt = ''.join(opts[0])    
        if opt not in allowed:
            print "Invalid command line argument"
            sys.exit(1)
    
    # Make command call
    cmd = 'w ' + opt
    w = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)

    # wait for process to complete before printing
    stdout, stderr = w.communicate()
    print stdout
    

#if we run this as a program, execute this function
if __name__ == '__main__':        
    do_w()