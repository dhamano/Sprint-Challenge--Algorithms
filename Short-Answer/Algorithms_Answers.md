#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
    a = 0 is O(1)
    n*n evaluates to a number and n*n*n evaluates to a number which is O(1) constant time.
    while (a < n*n*n) conditional statement is O(n) since it is a loop
    the statement within the while loop is a multiplication with addtion so O(1) constant time.
    since we measure the greatest change in time we get O(n)


b) O(n^2)
    sum = 0 is O(1)
    the for loop is O(n) and has a while loop in it which is also O(n) so the total for the nested loop is O(n^2).
    j = 1 is O(1) as is j *= 2 and sum +=1.
    since we measure the greatest change in time we get 0(n^2)


c) O(n)
    if bunnies == 0 and return 0 and return 2 + bunnyEars(bunnies-1) are all O(1) operations.
    however, because it recurses upon itself it is a loop because as bunnies increase the number of recursions increase which puts the recusrive loop at O(n)

## Exercise II

_floor_ = 0

drop egg from _floor_:
    if egg does not break increment _floor_
        call drop egg from _flooor_
    else if egg breaks stop as eggs from this floor on will break.

the runtime complexity of this would be O(n) as we only have one loop assuming tha the floor the eggs break from changes.

if the floor the eggs break from is constant it would be O(1) since it would only go to the same floor everytime and would be constand. for example, if it was constant that floor 3 was the floor the eggs would break at, it doesn't matter how big n is, the loop will iterate only 4 times for floor 0, 1, 2, and 3. whereas if the floor changed you'd have to increment to whatever floor the break changed to.