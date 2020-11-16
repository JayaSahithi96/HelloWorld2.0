secret= 9
guess_count=0
while guess_count<3:
    guess = int(input("Guess:"))
    guess_count += 1
    if guess== secret:
        print('you won')
        break
else:
    print('you lost:C')


