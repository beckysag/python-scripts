import os
import sys
import urllib2


# Retreives an arbitrary file based on URL and saves it into a named file. 
def problem3():    
    if (len(sys.argv) != 3):
        sys.exit(1)
    # Get url of site from first arg
    url = sys.argv[1]
    # Get filename from second arg
    filename = sys.argv[2]
    
    # Check for http:// in website name  
    if not url.startswith('http://'):
        url = 'http://' + url
       
    out = open(filename, 'wb')    
    response = urllib2.urlopen(url)
    html = response.read()
    out.write(html)
    out.close()
   
    
#if we run this as a program, execute this function
if __name__ == '__main__':        
    problem3()

