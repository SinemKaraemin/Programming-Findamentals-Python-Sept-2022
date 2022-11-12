lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmets_broken = lost_fight_count // 2
total_swords_broken = lost_fight_count // 3
total_shields_broken = lost_fight_count // 6
total_armors_broken = total_shields_broken // 2

expenses = helmet_price * total_helmets_broken \
+ sword_price * total_swords_broken \
+ shield_price * total_shields_broken \
+ armor_price * total_armors_broken

print(f"Gladiator expenses: {expenses:.2f} aureus")