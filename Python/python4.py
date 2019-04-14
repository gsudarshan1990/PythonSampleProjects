#Cost of hosting the server per day
cost=0.51
number_of_hours=24
Total_cost_PerDay=cost*number_of_hours
print('The total expenses per day is {:.2f}'.format(Total_cost_PerDay))
#Cost of hosting the server per month
#Let us consider month has 31 days
Days_In_Month=31
Total_Cost_PerMonth=Total_cost_PerDay*31
print('Total expenses per month is {:.2f}'.format(Total_Cost_PerMonth))

Total_fund=918
Total_Number_of_days=Total_fund/Total_cost_PerDay
#Cost for twenty servers per day
servers=20
Total_Cost_for_TwentyServers=20*Total_cost_PerDay
print('Cost for twenty servers per day {:.2f}'.format(Total_Cost_for_TwentyServers))

#Cost for twenty servers per month
Total_Cost_for_TwentyServersPerMonth=20*Total_Cost_PerMonth
print('Cost for twenty servers per month {:.2f}'.format(Total_Cost_for_TwentyServersPerMonth))

#Total number of days
print('Number of days using 918 fund is {}'.format(Total_Number_of_days))

