import matplotlib.pyplot as plt


def unipolar(b):    # variable 'b' denotes binary input, 'e' denotes encoded output
    e=list(b)
    e.append(e[-1])  #appending the last element again to display a continous step function graph  
    return e


def nrz_l(b):
    e=list(b)
    e=[-1 if i==0 else 1 for i in e]# assigns -1 if the binary input is 0, 1 for binary input 1
    e.append(e[-1])
    return e



def nrz_i(b):
    e=list(b)
    
    for i in range(len(b)):
        if i==0:                                 #assuming that the signal was "high" before receiving binary input
           if b[i]==1:
              e[i]=-1        
              continue
           else:
              e[i]=1
              continue             
        if b[i]==1 and i!=0:             
            if e[i-1]==-1:
                e[i]=1
                continue
            else :
                e[i]=-1
                continue
        else:
            e[i]=e[i-1]       
    e.append(e[-1])
        
    return e


def polar_rz(b):
    li=list(b)
    li=[-1 if i==0 else 1 for i in b]
    e=[]
    for i in range(len(b)):
        e.append(li[i])
        e.append(0)                        #for appending '0s' between elements for mid-transition
    e.append(e[-1])    
    return e
def Biphase_manchester(b):
    e=[]
    for i in range(len(b)):
        if b[i]==1:                          # -1 to 1 to denote signal 1
            e.append(-1)
            e.append(1)
        else:
            e.append(1)                # 1 to -1 to denote signal 0
            e.append(-1)
    e.append(e[-1])        
    return e

def diff_manchester(b):
    e=[]
    for i in range(len(b)):
          if i==0:                        #assuming that the signal was high before receiving binary input
             if b[i]==0:
                 e.append(-1)
                 e.append(1)
                 
             else:
                 e.append(1)
                 e.append(-1)
                 
          else:
               if b[i]==1:
                   e.append(e[-1])
                   if e[-1]==1:
                       e.append(-1)
                   else:
                       e.append(1)

               else:
                   if e[-1]==-1:
                       e.append(1)
                       e.append(-1)
                   else:
                       e.append(-1)
                       e.append(1)
                        
    e.append(e[-1])         
    return e

def ami(b):
    e=[]
    first=1
    flag=0
    for i in range(len(b)):
            if b[i]==0:
                e.append(0)
            else:
                if first:
                    e.append(1)
                    flag=1
                    first=0
                else:
                    if flag==1:
                        e.append(-1)
                        flag=0
                    else:
                        e.append(1)
                        flag=1
    e.append(-1)
    return e


def pseudo(b):
    e=[]
    first=1
    flag=0
    for i in range(len(b)):
            if b[i]==1:
                e.append(0)
            else:
                if first:
                    e.append(1)
                    flag=1
                    first=0
                else:
                    if flag==1:
                        e.append(-1)
                        flag=0
                    else:
                        e.append(1)
                        flag=1
    e.append(-1)
    return e

                        
               
                         

def all_plot(c,b,bout):                 #to plot all the encoding techniques
    plt.subplot(5,2,1)
    plt.ylabel("Clock")
    plt.plot(c,color='black',drawstyle='steps-post',marker='>')
    plt.grid()
    plt.subplot(5,2,2)
    plt.ylabel("Input")
    plt.plot(bout,color='red',drawstyle='steps-post',marker='>')
    plt.grid()
    plt.subplot(5,2,3)
    plt.ylabel("Unipolar-NRZ")
    plt.plot(unipolar(b),color='red',drawstyle='steps-post',marker='>')
    plt.grid()
    plt.subplot(5,2,4)
    plt.ylabel("P-NRZ-L")
    plt.plot(nrz_l(b),color='red',drawstyle='steps-post',marker='>')
    plt.grid()
    plt.subplot(5,2,5)
    plt.ylabel("P-NRZ-I")
    plt.plot(nrz_i(b),color='red',drawstyle='steps-post',marker='>')
    plt.grid()
    plt.subplot(5,2,6)
    plt.ylabel("Polar-RZ")
    plt.plot(polar_rz(b),color='red',drawstyle='steps-post',marker='>')
    plt.grid()
    plt.subplot(5,2,7)
    plt.ylabel("B_Man")
    plt.plot(Biphase_manchester(b),color='red',drawstyle='steps-post',marker='>')
    plt.grid()
    plt.subplot(5,2,8)
    plt.ylabel("Dif_Man")
    plt.plot(diff_manchester(b),color='red',drawstyle='steps-post',marker='>')
    plt.grid()
    plt.subplot(5,2,9)
    plt.ylabel("Bipolar_AMI")
    plt.plot(ami(b),color='red',drawstyle='steps-post',marker='>')
    plt.grid()
    plt.subplot(5,2,10)
    plt.ylabel("Bipolar_pseudoternary")
    plt.plot(pseudo(b),color='red',drawstyle='steps-post',marker='>')
    plt.grid()
    plt.show()




   
choice = 'y'
print("Enter the number of bits in encoded data : ")   
size=int(input())
b=[]
print('Enter the binary bits sequnce of length ',size,' bits : \n')
for i in range(size):
    print('Enter element ',i+1,' :')
    b.append(int(input()))
c=[]
bout= list(b)
bout.append(bout[-1])
for i in range(2*size+1):                   #block to compute clock signal based on input size
    if(i%2==0):
        c.append(int(1))
    else:
        c.append(int(0))    
    
while (choice =='Y' or choice =='y'):    
    print("\nWhich type of encoding do you want to perform : ")
    print("         1->UNIPOLAR:")
    print("         2->NRZ-L:")
    print("         3->NRZ-I:")
    print("         4->POLAR RZ:")
    print("         5->MANCHESTER:")
    print("         6->Differential Manchester:")
    print("         7->Bipolar AMI:")
    print("         8->Bipolar pseudoternary:")
    print("         9->ALL:")
    print("Enter your choice (1-9): ", end="")
    y = int(input())
    
    if y == 1:
       plt.subplot(3,1,1)
       plt.ylabel("Clock")
       plt.plot(c,color='black',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.subplot(3,1,2)
       plt.ylabel("Input data")
       plt.plot(bout,color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.subplot(3,1,3)
       plt.ylabel("Unipolar-NRZ")
       plt.plot(unipolar(b),color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.show()

    elif y == 2:
       plt.subplot(3,1,1)
       plt.ylabel("Clock")
       plt.plot(c,color='black',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.subplot(3,1,2)
       plt.ylabel("Input data")
       plt.plot(bout,color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.subplot(3,1,3)
       plt.ylabel("polar-NRZ-L")
       plt.plot(nrz_l(b),color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.show()

    elif y == 3:
       plt.subplot(3,1,1)
       plt.ylabel("Clock")
       plt.plot(c,color='black',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.subplot(3,1,2)
       plt.ylabel("Input data")
       plt.plot(bout,color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.subplot(3,1,3)
       plt.ylabel("polar-NRZ-I")
       plt.plot(nrz_i(b),color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.show()

    elif y == 4:
       plt.subplot(3,1,1)
       plt.ylabel("Clock")
       plt.plot(c,color='black',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.subplot(3,1,2)
       plt.ylabel("Input data")
       plt.plot(bout,color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.subplot(3,1,3)
       plt.ylabel("polar-RZ")
       plt.plot(polar_rz(b),color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.show()

    elif y == 5:
       plt.subplot(3,1,1)
       plt.ylabel("Clock")
       plt.plot(c,color='black',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.subplot(3,1,2)
       plt.ylabel("Input data")
       plt.plot(bout,color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.subplot(3,1,3)
       plt.ylabel("Biphase Manchester")
       plt.plot(Biphase_manchester(b),color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.show()

    elif y == 6:
       plt.subplot(3,1,1)
       plt.ylabel("Clock")
       plt.plot(c,color='black',drawstyle='steps-pre',marker='>')
       plt.grid()
       plt.subplot(3,1,2)
       plt.ylabel("Input data")
       plt.plot(bout,color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.subplot(3,1,3)
       plt.ylabel("Differential-Manchester")
       plt.plot(diff_manchester(b),color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.show()


       
    elif y == 7:
       plt.subplot(3,1,1)
       plt.ylabel("Clock")
       plt.plot(c,color='black',drawstyle='steps-pre',marker='>')
       plt.grid()
       plt.subplot(3,1,2)
       plt.ylabel("Input data")
       plt.plot(bout,color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.subplot(3,1,3)
       plt.ylabel("Bipolar_AMI")
       plt.plot(ami(b),color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.show()

    elif y == 8:
       plt.subplot(3,1,1)
       plt.ylabel("Clock")
       plt.plot(c,color='black',drawstyle='steps-pre',marker='>')
       plt.grid()
       plt.subplot(3,1,2)
       plt.ylabel("Input data")
       plt.plot(bout,color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.subplot(3,1,3)
       plt.ylabel("Bipolar_pseudoternary")
       plt.plot(pseudo(b),color='red',drawstyle='steps-post',marker='>')
       plt.grid()
       plt.show()   
    elif y == 9:
       all_plot(c,b,bout)   

    else:
        print("INVALID CHOICE, TRY AGAIN!!!")

    print("Do you want to try again? (y/n) : ", end="")
    choice = input()
    

quit()
 










