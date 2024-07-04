import random as rd
#profit for each month
def profits_calcular():
    revenue = [rd.randint(a=1200,b=12030)+rd.random() for i in range(365)]
    expenses = [rd.randint(a=10,b=1234) + rd.random() for i in range(365)]
    monthlyRevenue = 0
    monthlyExpenses = 0
    monthlyProfits = []
    for i in range(365):
        monthlyRevenue += revenue[i]
        monthlyExpenses += expenses[i]
        if ((i+1)%30==0):
            monthlyProfits.append(round(monthlyRevenue-monthlyExpenses,ndigits=4))
            monthlyExpenses = 0
            monthlyRevenue = 0
    return monthlyProfits
    
#profit after taxes
def calculate_profit_taxes():
    monthly_profits = profits_calcular()
    months = [round(profit * 0.7, 4) for profit in monthly_profits]
    return months

#profit margin
def profit_margin():
    profit_taxes = calculate_profit_taxes()
    revenues = [rev/3 for rev in profit_taxes]
    profit_margin = [round(profit/revenue) for profit in profit_taxes]

#best month
def best_month():
    profits = calculate_profit_taxes()
    mayor = 0
    for i,p in enumerate(profits):
        if p > mayor:
            mayor = p
            indice = i
    return indice,mayor


print(best_month())
    
