'''
Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200
'''

num_shoes = int(input())
sizes_available = input().split()
customers = int(input())
customer_order = []

total_sold = 0

for _ in range(customers):
    order = input().split()
    size = order[0]
    price = int(order[1])
    customer_order.append([size, price])
# customer_order = [('6', '55'), ('6', '45'), ('6', '55'), ('4', '40'), ('18', '60'), ('10', '50')] 6 indecies

for i in range(customers):
    to_be_removed = customer_order[i][0]
    if customer_order[i][0] in sizes_available:
        sizes_available.remove(to_be_removed)
        total_sold += customer_order[i][1]

print(total_sold)
