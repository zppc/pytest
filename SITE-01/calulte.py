import  math
def calut( ):
    result=0
    for  i in  range(1,40):
        result+= i**-1*(i+1)**-1
    return result


def  main():

    result= calut()
    print result

if  __name__=="__main__":
    main()
