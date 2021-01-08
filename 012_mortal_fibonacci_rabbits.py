def mortal_fibonacci(months, die_after):
    ages = [0] * die_after              # Array representing the number of rabbits in every age
    ages[-1] = 1                        # Initializing the array with 1 rabbit with x months to live
    for _ in range(1, months):          # Iterating over # of months
        new_rabbits = sum(ages[:-1])    # Qty of Newborns
        ages[:-1] = ages[1:]            # Shift ages left, or rabbits getting older
        ages[-1] = new_rabbits          # Assigning newborns
    return sum(ages)                    # returning the number of alive rabbits after x months


if __name__ == '__main__':
    coelhos = mortal_fibonacci(93, 20)
    print(coelhos)
