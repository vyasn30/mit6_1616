import pytest


def calculate_savings(current_savings: float, annual_salary:float, saving_percent_salary:float, total_cost_house:float):
    try:
        down_payment = 0.25 * total_cost_house
        print(f"Downpayment needed is {down_payment}")
        annual_returns_rate = 0.04
        diff_dp = down_payment - current_savings

        saving_months = 0

        # print(diff_dp<=0)

        while (down_payment - current_savings)>=0:
            """
            Breaks when I can pay dp
            """
            monthly_savings = (annual_salary/12)*saving_percent_salary
            current_savings +=  monthly_savings #Monthly savings

            current_savings += (current_savings*annual_returns_rate)/12 #Interest
            # print(current_savings)
            diff_dp -= monthly_savings
            saving_months += 1


        return saving_months

    except ValueError as e:
        print(e)


def main():
    annual_salary = float(input("Enter annual salary: "))
    percent_salary = float(input("Enter the percent of your salary to save, as a decimal:"))
    cost_home = float(input("Enter the cost of your dream home:"))
    current_savings = float(input("Enter current savings"))


    calculate_savings(
        current_savings=current_savings,
        annual_salary=annual_salary,
        saving_percent_salary=percent_salary,
        total_cost_house=cost_home
    )



def test_calculate_savings():
    
    ans = calculate_savings(
        current_savings=0,
        annual_salary=120000,
        saving_percent_salary=.10,
        total_cost_house=1000000
    )

    assert ans == 182