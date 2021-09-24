import time
import pandas as pd

# def database():
lb = pd.DataFrame({'Name': ['John', 'Mary', 'Ben'],
               'Age': ['14', '61', '17'],
               'Weight': [65, 45, 70],
               'Height': [178, 148, 165],
               '5km time': [40, 50, 25]})
# fivek_update = lb.sort_values(['5km time'], ascending=[True])
# print(fivek_update)

def new_entry():
    user_name = (input("Enter name: "))
    user_height = float(input("Enter height (cm): "))
    user_weight = float(input("Enter weight (kg): "))
    user_age = int(input("Enter your age: "))
    input("Press enter to start run")
    start_time = time.time()
    input("Press enter to finish run")
    stop_time = time.time()
    time_lapsed = stop_time - start_time
    new_row = {'Name': user_name, 'Age': user_age, 'Weight': user_weight, 'Height': user_height, '5km time': time_lapsed}
    lb_update = lb.append(new_row, ignore_index=True)
    print(lb_update)
    # return time_lapsed


def alarm_stopwatch():
    input("Press enter to start run")
    start_time = time.time()
    input("Press enter to finish run")
    stop_time = time.time()
    time_lapsed = stop_time - start_time
    print(time_lapsed)


# main_menu()
new_entry()