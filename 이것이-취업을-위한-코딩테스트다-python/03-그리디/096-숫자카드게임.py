n, m = map(int, input().split())
cards = [list(map(int, input().split()))for _ in range(n)]

max_card = 0

for cardset in cards:
    if max_card < min(cardset):
        max_card = min(cardset)

print(max_card)