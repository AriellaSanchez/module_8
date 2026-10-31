#self-assessment questions: 1.The first bug I noticed was missing : after the for loop statement. I found it from the traceback because python pointed out the syntax error. This tells me I can recognize these basic errors and figure out what to do on my own first.  2.Apply_discount(price, tier) takes a price and a customer tier as inputs and it determines the appropriate discount based on the tier. Then it returns the price after the discount has been applied.A collegue could use it without reading the body if the function name, parameters, and return value are all provided.   3. AI disclosure: I used AI to help me with exercise 5 on this lab as instructed while debugging. I looked at the suggestions and made sure I unerstood what the error was and how to fix it on my own though.

#exercise 1
#define calculate tax function
def calculate_tax(price,rate):
    return price * rate

#calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on 100 at 7%: ${tax1:.2f}") #7.00
print(f"Tax on 250 at 8%: ${tax2:.2f}") #20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") #7.50

#exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

#calling the function
price = 200
tiers = ["gold", "silver", "bronze", "none"]

#for loop
for tier in tiers:
    print(f"{tier}: ${apply_discount(price,tier):.2f}")

#exercise 3
#write it out manually first, then refactor into a function
discounted = apply_discount(200, "gold") #used below
tax = calculate_tax(discounted, 0.07)
after_tax = discounted  + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

#refactor into a function
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax
print(f"Final price: ${final_price(200, "gold", 0.07):.2f}")

#exercise 4
orders = [(200,"gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: ${tier}, Final: ${total:.2f}")

#exercise 5
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    #print("sale=", sale)
    total += sale
    #print("total=", total)
print(f"Total: ${total}")
#I need to add each sale to the running total instead of replacing the total

count = 0
for sale in sales:
    count += 1
    #print("count=", count)
print(f"Count: {count}")
#I need to add : to the end of line 69 because it's a for loop

i = 0
while i < len(sales):
    #print("i=", i)
    print(sales[i])
    i += 1
#I need to stop before i reaches the length of the list because the index doesn't exist

#exercise 6
x = 100 #apple # Global
def double_it():
    x = 999 #another apple (not the same apple as above)
    return x * 2
print(x)
print(double_it())
print(x)

