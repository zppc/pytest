#-*-coding:utf-8-*-
import random



def main():
    result=[0,0,0,0,0,0]
    pass
    rol_qty=input("请输入抛投次数:")
    for i in range(rol_qty):
        roll=random.randint(1,6)
        result[roll-1]=result[roll-1]+1
    # for  j in range(1,len(result)+1):
    #     print("{}抛到{}次".format(j,result[j-1]))
    for key, vaule in enumerate(result):
        print("{}抛到{}次".format(key+1,vaule))

if __name__=="__main__":
    main()