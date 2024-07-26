# goatRace kata
# takes in a string with three name - time pairs
# should return a dictionary with firstplace key, goatwithlongestname key and average time key
# if there's a draw, whichever the alphabetically first named goat wins

def goat_race(str) :
    report = {}
    return report

def first_place(goats) :
    update_goats = {**goats}
    goat_keys = update_goats.keys()
    numbers = []
    lookup = {}
    for goat in goat_keys :
        split_str = update_goats[goat].split(':')
        joined = ''.join(split_str)
        number_number = int(joined)
        numbers.append(number_number)
        lookup[number_number] = goat
    fastest_time = min(numbers)
    fastest_goat = lookup[fastest_time]
    fastest_time_string = update_goats[fastest_goat]

    return {fastest_goat: fastest_time_string}