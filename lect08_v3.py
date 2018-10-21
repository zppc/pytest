#-*-coding:utf-8-*-
import random
import matplotlib.pyplot as plt


def main():
    result=[0]*12
    roll_list=list(range(2,13))
    result_dict=dict(zip(roll_list,result))
    rol_qty=input("请输入抛投次数:")
    xlist=[]#第几次抛
    ylist1=[]#每次抛的点数
    ylist2 = []  # 每次抛的点数
    for i in range(rol_qty):
        roll1=random.randint(1,6)
        roll2=random.randint(1,6)
        roll=roll1+roll2
        result_dict[roll]+=1
        xlist.append(i+1)
        ylist1.append(roll1)
        ylist2.append(roll2)
    # for  j in range(1,len(result)+1):
    #     print("{}抛到{}次".format(j,result[j-1]))
    for key, vaule in result_dict.items():
        print("{}抛到{}次,所占比率:{}".format(key,vaule,vaule/rol_qty))

    plt.scatter(xlist,ylist1,label='First',c='red',marker='o',alpha=0.5)
    plt.scatter(xlist, ylist2,label='Second',c='green', marker='o', alpha=0.6)
    plt.xlabel('N times')
    plt.ylabel('Number')
    plt.legend()
    plt.show()



if __name__=="__main__":
    main()