#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import Tkinter

def changer() :
    global x ;
    x = 3;
    y = 5;
    return y;
def createlist(len) :
    list = range(len);
    return list;
def payment_per_month(times, total_amount, rate) :
    coeffient_1 = pow((1 + rate), times);
    payment = (coeffient_1 * total_amount * rate) / (coeffient_1 - 1);
    return payment;
def capital_left_per_month(capital, rate, payment) :
    capital_left = capital * ( 1 + rate) - payment;
    return capital_left;
def interest_per_month(capital_left, rate) :
    interest = capital_left * rate;
    return interest;
    
def align_yaxis(ax1, v1, ax2, v2):
    """adjust ax2 ylimit so that v2 in ax2 is aligned to v1 in ax1"""
    _,y1 = ax1.transData.transform((0, v1)) 
    _,y2 = ax2.transData.transform((0, v2)) 
    inv = ax2.transData.inverted()
    _,dy = inv.transform((0, 0)) - inv.transform((0, y1-y2)) 
    print ("y1 =%d, y2=%d, dy=%d"%(y1, y2, dy))
    miny, maxy = ax2.get_ylim()
    ax2.set_ylim(miny+dy, maxy+dy) 
    

    
def calculate_my_interest_per_month(rate, times, total_amount) :
    payment = payment_per_month(times, total_amount, rate);
    capital = total_amount;
    capital_left_list = createlist(times)
    times_list = createlist(times)
    interest_list=createlist(times)
    capital_list = createlist(times)
    
    figure=plt.figure(figsize=(20,15))
    ax1 = figure.add_subplot(111)
    ax2 = ax1.twinx()
    ax2.set_ylim(0.0, 15000.00)
    plt.xlim(0, 240)
    ax1.grid("on", "both");
    ax1.minorticks_on()
    ticks = np.arange(0, 240, 1)
        
    plt.xlabel("Month(s)")
    plt.ylabel("RMB")
    plt.title("My Loan")
    mile_stone_flag = -1
    mile_stone = 0;
    interest_point = 0.0
    money = 13000;
    
    for i in range(0, times) :
        interest = interest_per_month(capital,rate);
        interest_list[i]=interest
        capital = capital_left_per_month(capital, rate, payment)
        capital_left_list[i]=capital / 100;
        capital_list[i] = payment - interest
        #print "interest = %d, money=%d"%(interest, (payment-interest))
        if(interest >= (payment - interest)) :
            mile_stone_flag = -1;
        elif((interest <= (payment - interest)) and (mile_stone_flag== -1)):
            #print "#################################"
            mile_stone_flag = 0;
            mile_stone = i;
            money = payment - interest;
            interest_point = interest;
               
            
        #print "month = %d capital = %02f, interest = %02f"%(i + 1, capital, interest);
        
    ax1.plot(times_list,capital_left_list,color="red",linewidth=2, label="capital_left x 100")
    ax1.plot(times_list,interest_list,"b--", label="interest")
    ax1.plot(times_list, capital_list,label="capital", color="green", linewidth=2 )
    align_yaxis(ax2, 0, ax1, 0)
    
    bbox = dict(boxstyle="round", fc="0.8")
    offset = 50
    arrowprops = dict(
    arrowstyle = "->",
    connectionstyle = "angle,angleA=0,angleB=90,rad=10")
    #print "milestone =%d, payment =%d"%(mile_stone, payment)
    ax1.annotate('mile_stone:%d month\ncapital: %f\ninterest: %f'%(mile_stone, money, interest_point),
            (mile_stone, money), xytext=(-3*offset, offset), textcoords='offset points',
            bbox=bbox, arrowprops=arrowprops)

    ax1.legend()
    plt.savefig("my_load.pdf")
    plt.show()
 

   
calculate_my_interest_per_month(0.0704 / 12, 240, 1300000.00);






