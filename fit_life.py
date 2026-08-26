WATER_PER_KG = 30
ML_IN_LITER = 1000
SEPARATOR = '-' * 30

print('Welcome to the FitLife!')
print(SEPARATOR)

user_name = input('What is your name? ').title()
print(
    f'Nice to meet you, {user_name}! '
    'Now answer a few questions about yourself:')

user_age = int(input('How old are you? Enter your age in full years: '))
user_weight = float(
    input('What is your weight? (kg) ').replace(',', '.')
)
user_height = float(
    input('What is your height? (m) ').replace(',', '.')
)

# body mass index calculation
bmi = round(user_weight / (user_height ** 2), 1)

# water intake calculation
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_IN_LITER

print(SEPARATOR)
print(f'Report for the user: {user_name} ({user_age} y.o.)')
print(f'Your Body Mass Index: {bmi}')
print(f'Recommended daily water intake: {water_l:.2f} l')
print()
print('Calculation complete. Stay healthy!')
