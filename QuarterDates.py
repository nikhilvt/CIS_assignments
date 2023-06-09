
# def DateQuarter(date,quarter):
#     date=int(date)
#     previous_month= date-1
#     print(previous_month,quarter)
#     # quarter=int(quarter)
#     # previous_quarter=(quarter-1,date)
#     date= str(date)
#     year=date[:-2]
#     year=int(year)
#     #print(year)
#     month=date[-2:]
#     month=int(month)
#     #print(month)
#     future_month=(year+1,month+1)
#     future_month=str(future_month)
    
    

#     print(future_month)

    
   
# DateQuarter('202208','q3') 

# # def DateQuarter(date,quarter):

#     dict[Q1]=1,2,3
#     dict[Q2]=4,5,6
#     dict[Q]=7,8,9
#     dict[Q4]=10,11,12

#     date= int(date)
#     previous_month=date-1
    
#     print(previous_month,quarter)

    


# DateQuarter('202208','Q4')


    




# def DateQuarter(date,quarter):
#     year=int(date[:4])
#     month=int(date[4:]) 
#     if month==1:
#         previous_month= str(year-1)+ '12'
#        # print(previous_month)
#     else:
#         previous_month= str(year)+str(month-1).zfill(2)
#         #print(previous_month)
#     if quarter == 'Q1':
#         previous_quarter='Q4_'+str(year-1)
#         #print(previous_quarter)
#     else:
#         previous_quarter_number=int(quarter[1])-1
#        # print(previous_quarter_number)
#         previous_quarter='Q'+str(previous_quarter_number)+'_'+str(year)
#         #print(previous_quarter)
#     future_month = str(year+1)+str(month-1).zfill(2)

#     #print(future_month)

#     current_quarter= str(quarter) +'_'+str(year)
#     #print(current_quarter)

#     ouput= {
#         'previous_month': previous_month,
#         'previous_quarter' : previous_quarter,
#         'future_month' : future_month,
#         'current_quarter': current_quarter
        
#     }
#     print(ouput) 
# DateQuarter("202208","Q1")





def DateQuarter(date,quarter):
    year=int(date[:4])
    month= int(date[4:])
    # print(year)
    # print(month)
    if month==1  :
        previous_month= str(year-1)+'12'
        #print(previous_month)
    else:
        previous_month=str(year)+str(month-1).zfill(2)
        #print(previous_month)
    Current_quarter=quarter+"_"+str(year)
    print(Current_quarter)
    if quarter=="Q1":
        previous_quarter= "Q4"+"_"+str(year-1)
        #print(previous_quarter)
    else:
        quarter_number=int(quarter[1:])
        #print(type(quarter_number))
        previous_quarter ="Q"+str(quarter_number-1)+"_"+str(year)
        #print(previous_quarter)
    future_month= str(year+1)+str(previous_month[-2:])
    #print(future_month)


    dict = {
        'previous_month': previous_month,
        'current_quarter': Current_quarter,
        'previous_quarter': previous_quarter,
        'futureyear_month':future_month
    }

    print(dict)

DateQuarter("202208","Q3")

    