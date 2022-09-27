import sys
input = sys.stdin.readline

n = int(input())
movie = 666
movies = [movie]
while len(movies) < n:
    movie += 1
    if '666' in str(movie):
        movies.append(movie)

print(movies[-1])