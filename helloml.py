name = input("Enter your name:")
age = int(input("Enter your age:"))
if name == "":
    print("invalid name")
else:
    print(name)

if age <=0 or age>120:
    print("invalid age")
else:
    print(age)




movies_list = ["vamshi","sahukara","appu","abhi","yuvaratna"]
if "bindass" not in movies_list:
    movies_list.append("bindass")
else:
    print("movie name present in list")
if "sahukara" in movies_list:
    movies_list.remove("sahukara")
movies_list.sort()
print(movies_list)

for i in range(1,101):
    if i%2 == 0 and i%10!=0:
        print(i)

my_dict = {
    "name":"venki",
    "age":14,
    "skills":"python",
}

if my_dict['age']>=18:
   my_dict["is_adult"] = True
else:
    my_dict["is_adult"] = False

print(my_dict)


def check_skill_level(skill):
    if skill == "python":
        print("good choice,keep going")
    elif skill == "java":
        print("Strong Language,good for careers")
    else:
         print("Explore this skill more.")

skill = input("enter your skill:").lower()
check_skill_level(skill)

numbers = [12, 7, 45, 22, 100, 3, 89, 40, 10]

evens = []
odds = []
greater50 = []
div5 = []

for i in numbers:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)

    if i > 50:
        greater50.append(i)

    if i % 5 == 0:
        div5.append(i)

print("Even numbers:", evens, "Count:", len(evens))
print("Odd numbers:", odds, "Count:", len(odds))
print("Numbers >50:", greater50, "Count:", len(greater50))
print("Divisible by 5:", div5, "Count:", len(div5))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
if is_prime(n):
    print("Prime")
else:
    print("Not Prime")




        
        

    



