stalls = "aaababbaab"
quantity_milk_from_stall = 0
total_milk = 0
for stall in stalls:
    quantity_milk_from_stall += 2
    if stall == 'b':
        total_milk += quantity_milk_from_stall

print(f'Произведено молока за день: {total_milk}')