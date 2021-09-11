import sys

def main() :
    n = int(input())
    people = list(map(int, sys.stdin.readline().split()))
    hour = [0 for i in range(n) ] 
    people.sort()

    hour[0] = people[0]
    for i in range(1, n) :
        hour[i] = hour[i-1] + people[i]

    print(sum(hour))

if __name__ == "__main__" :
    main()
