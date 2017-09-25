#this is a pgm for a timer
import time
import webbrowser

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#When the value of a list part contains the string %s,
#then it is interpreted as a literal browser command line to be used with the argument URL substituted for %s;
#if the part does not contain %s, it is simply interpreted as the name of the browser to launch.

url = 'https://www.google.com'  


#putting the program in loop
count = 0
while (count < 3):
    time.sleep(10)
    webbrowser.get(chrome_path).open(url), count  #opens the needed url in chrome
    count = count + 1
print ('Done')  #prints done after loop

