import webbrowser
fname_list=[]
lname_list=[]
name=[]

Datafile=open("customerdata.txt","r")
l=Datafile.read().split()                                         
l=list(l)                                                           
for i in range(0,4):                                               
    l.pop(0)
new_list=[l[i:i+5] for i in range(0,len(l),5)]                      
def orders():                                                       
   print("\n")
   print("Total number of orders: ",end=" ")
   print(len(new_list))
def totalAmount():                                                       
    total_amount=0
    for i in range(0,len(new_list)):
        total_amount = total_amount + int(new_list[i][4])
    print("Total amount of all the orders: ", end=" ")
    print(total_amount)
def orderedOnce():                                                
    print("List of customers who ordered once and did not order again:")
    for i in range(0,len(new_list)):
        fname_list.append(new_list[i][2])
    for i in range(0,len(new_list)):
        lname_list.append(new_list[i][3])
    for i in range(0,len(fname_list)):
        #logic to combine first and last name.
        name.append(fname_list[i]+ ' ' +lname_list[i])             
        name[i]=name[i].replace(',', '')
    oneTrans=0
    twoTrans=0
    threeTrans=0
    fourTrans=0
    fiveTrans=0
    for i in range(0,len(name)):
        if name.count(name[i])==1:
            oneTrans+=1
            print(name[i])
    for i in range(0,len(name)):
        if name.count(name[i])==2:
            twoTrans+=1
    nc2=int(twoTrans/2)
    for i in range(0,len(name)):
        if name.count(name[i])==3:
            threeTrans+=1           
    nc3=int(threeTrans/3)
    for i in range(0,len(name)):
        if name.count(name[i])==4:
            fourTrans+=1
    nc4=int(fourTrans/4)
    for i in range(0,len(name)):
        if name.count(name[i])>=5:
            fiveTrans+=1
    nc5=int((fiveTrans/5)-6)
    fileData = """
                    <table border=1 cellspacing="1px">
                        <tr>
                            <th>No of Orders</th>
                            <th>Count of Customers</th>
                        </tr>
                        <tr>
                            <td>1</td>
                            <td>{One}</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>{Two}</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td>{Three}</td>
                        </tr>
                        <tr>
                            <td>4</td>
                            <td>{Four}</td>
                        </tr>
                        <tr>
                            <td>5+</td>
                            <td>{FivePlus}</td>
                        </tr>
    </table>
    """.format(One=oneTrans,Two=twoTrans,Three=threeTrans,Four=fourTrans,FivePlus=fiveTrans)
    writeFile=open("Demo.html","w")
    writeFile.write(fileData)
    writeFile.close()
webbrowser.open("Demo.html")   

if __name__ == '__main__':
    orders()
    totalAmount()
    orderedOnce()

Datafile.close()