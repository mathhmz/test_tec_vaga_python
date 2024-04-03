if __name__ == '__main__':
    
    perf_var = 12
    time_spent = int(input("tempo gasto na viagem"))
    averg_speed = int(input("velocidade média durante a mesma"))
    
    distance = time_spent * averg_speed
    
    fuel_used = distance / perf_var

    
    print(f"{fuel_used:.3f}")