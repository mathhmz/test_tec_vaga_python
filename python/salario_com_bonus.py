if __name__ == '__main__':
    
    seller = str(input())
    salary = float(input())
    sold_in_cash = float(input())
    

    total_salary = salary + (sold_in_cash * 0.15)
    

    
    print(f"TOTAL = R$ {total_salary:.2f}")