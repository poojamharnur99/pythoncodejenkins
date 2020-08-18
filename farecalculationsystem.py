#Fair Calculation system for railway

#function to calculate first class ticket
def calculate_ticket_for_first_class(no_of_passangers):
    one_passanger_fare=400                         #variable one_passanger_fare :fare for 1 passanger
    percent_gst_per_passanger=5                    #variable percent_gst_per_passanger: GST tax on each passanger
    GST_on_ticket = (one_passanger_fare * percent_gst_per_passanger) / 100 #it calculate gst per ticket
    total_first_class_ticket_amount= no_of_passangers * (one_passanger_fare + GST_on_ticket)  #calculate total  fare for first class
    return total_first_class_ticket_amount

#function to calculate general class ticket
def calculate_ticket_for_general_class(no_of_passangers):
    one_passanger_fare=300             #variable one_passanger_fare :fare for 1 passanger
    percent_gst_per_passanger=3        #variable percent_gst_per_passanger: GST tax on each passanger
    GST_on_ticket = (one_passanger_fare * percent_gst_per_passanger) / 100 #it calculate gst per ticket
    total_first_class_ticket_amount= no_of_passangers * (one_passanger_fare + GST_on_ticket)  #calculate total  fare for general class
    return total_first_class_ticket_amount

 # function to check number of passanger and class choise should be integer
def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

# main function to calculate fare
# variable no_of_passanger: booking ticket for how many passanger
# variable class_to_travel: this variable is used for first or second class booking

def calculare_fare(no_of_passangers,class_to_travel):
    result=0                                         # variable for final amount to pay to book ticket
    try:
        if is_integer_num(class_to_travel) and is_integer_num(no_of_passangers):
            if class_to_travel == 1 :                       #choise is one for first class
                result=calculate_ticket_for_first_class(no_of_passangers)   # call function to calculate first class fare
            elif class_to_travel == 2 :                     #choise is one for general class
                result=calculate_ticket_for_general_class(no_of_passangers) # call function to calculate general class fare
            else :
                print("Invalid Choise! ticket will not book for this choise ") #this will execute if choise is other than 1 and 2
            return result

    except TypeError:
        print('choise of class and number of passanger not integer TypeError Exception Raised')
        return None


