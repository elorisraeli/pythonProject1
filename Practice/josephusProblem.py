print("Solution to Josephus problem:")


# the problem is here in this link:
# https://he.wikipedia.org/wiki/%D7%91%D7%A2%D7%99%D7%99%D7%AA_%D7%99%D7%95%D7%A1%D7%A4%D7%95%D7%A1

# internet solution:

def who_goes_free(num_of_people, steps):
    list = []
    # because "range" get an array with 0 and length-1, its the little solution for this.
    total_people = range(num_of_people + 1)[1:num_of_people + 1]
    for i in total_people:
        list.append(i)
    print(list)
    counter = steps - 1
    while len(list) > 1:
        index_counter = counter % len(list)
        list.pop(index_counter)
        counter += steps - 1
        counter = counter % len(list)
    return list[0]


person = who_goes_free(41, 2)
print(person)
print("The person who goes free is: %d" % person)

