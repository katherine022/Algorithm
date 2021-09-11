import sys
import heapq

inf = sys.stdin

N = int(inf.readline().strip('\n'))
card = []
ans = 0

for _ in range(N) :
    heapq.heappush(card, int(inf.readline().strip('\n')))

while len(card) > 1 :
    card1 = heapq.heappop(card)
    card2 = heapq.heappop(card)

    sum_card = card1 + card2
    ans += sum_card

    heapq.heappush(card, sum_card)    

print(ans)
