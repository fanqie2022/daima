def ability_growth(days):
    initial_ability = 1
    growth_rate = 0.01
    cycle_days = 7
    continuous_learning_days = 3

    for day in range(1, days + 1):
        if day % cycle_days == 1:
            ability = initial_ability
        elif day % cycle_days <= continuous_learning_days:
            ability *= (1 + growth_rate)
        else:
            ability = initial_ability
        print(f"Day {day}: Ability = {ability:.2f}")

# 输出未来10年的能力值
ability_growth(10)