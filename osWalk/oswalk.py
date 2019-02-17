import fnmatch
import os
import time
 
rootPath = '/'
pattern = 'cat.jpg'
start_time = time.time()
 
for root, dirs, files in os.walk(rootPath):
  for filename in fnmatch.filter(files, pattern):
    if time.time() - start_time> 60:  #time out after 60 seconds
      break
    print( os.path.join(root, filename))