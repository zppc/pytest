#-*-coding:utf-8-*-
import random



def main():
    result=[0]*12
    roll_list=list(range(2,13))
    result_dict=dict(zip(roll_list,result))
    rol_qty=input("请输入抛投次数:")
    for i in range(rol_qty):
        roll1=random.randint(1,6)
        roll2=random.randint(1,6)
        roll=roll1+roll2
        result_dict[roll]+=1
    # for  j in range(1,len(result)+1):
    #     print("{}抛到{}次".format(j,result[j-1]))
    for key, vaule in result_dict.items():
        print("{}抛到{}次,所占比率:{}".format(key,vaule,vaule/rol_qty))

if __name__=="__main__":
    main()