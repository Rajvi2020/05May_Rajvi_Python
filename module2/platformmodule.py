import platform
#print(platform.architecture())
print(platform.machine())
print(platform.platform())

print(platform.
      python_version())

'''import platform
System અને Python વિશેની માહિતી મેળવવા માટે platform module import કરે છે.
platform.architecture()
Python interpreter 32-bit છે કે 64-bit તે બતાવે છે.

Example Output:

('64bit', 'WindowsPE')
platform.machine()
Computer ની processor architecture બતાવે છે.

Example Output:

AMD64
એટલે 64-bit processor architecture.
platform.platform()
Operating System ની સંપૂર્ણ માહિતી આપે છે.

Example Output:

Windows-11-10.0.26100-SP0
platform.python_version()
હાલમાં ચાલતું Python version બતાવે છે.

Example Output:

3.13.5
Quick Revision
Method	Use
platform.architecture()	Python 32-bit કે 64-bit છે તે બતાવે
platform.machine()	Processor architecture બતાવે
platform.platform()	Operating System ની માહિતી આપે
platform.python_version()	Python version બતાવે'''