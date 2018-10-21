# -*- coding: utf-8 -*-

from  multiprocessing import Pool
 
import  os,time,random

def work(msg):
    t_start=time.time()
    print("%s开始执行,进程号为%d"%(msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop =time.time()
    print(msg,"end%0.2f"%(t_stop-t_start))
	
pool = Pool(3)
for  i  in  range(0,10):
      pool.apply_async(work,(i,))
	  
 
print('start')
pool.close()
pool.join()
print('end')
 