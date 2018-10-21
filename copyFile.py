#-*- coding uft-8 -*-
from multiprocessing  import  Pool,Manager,Queue
import os 
def copyTask(name,oldfielddir,newfielddir,queue):

     fr =os.open(oldfielddir+"/"+name)
     fw = os.open(newfielddir+"/"+name,"w")
     context= fr.read()
     fw.write(context)

     fr.close()
     fw.close()
     queue.put(name)


def main():
    # 1.取得要copy的文件夹
    oldfielddir = input("请输入要复制的文件夹：")
    # 2.复制文件夹
    newfielddir = os.mkdir(oldfielddir + "复制")
    # 3.读到文件夹中的文件
    names = os.listdir()
    # 4 通过多进程复制文件
    pool = Pool(5)
    queue = Manager().Queue()
    for name in names:
        pool.apply_async(copyTask, arg=(name,oldfielddir, newfielddir, queue))
    allnum =  len(names)
    num = 0
    while num<=allnum:
        queue.get()
        num+=1
        radio= num / allnum*100
        print("已完成%f%%"%(radio))

if  __name__=="__main__":
    main()
