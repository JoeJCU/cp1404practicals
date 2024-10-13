import random

user_quick_picks = int(input("Enter the number of quick picks you would like: "))
random_num_list = []

for i in range(user_quick_picks):
    random_num = random.sample(range(1, 46), 6)  # 6 random nums
    print(random_num)
    for num in range(i):
        random_num_list.append(random_num)
