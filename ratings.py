"""Restaurant rating lister."""
# put your code here

# dictionary_name[key] = value

    # for line in scores_txt:
    #     line = line.rstrip()
    #     restaurant, score = line.split(":")
    #     scores[restaurant] = int(score)

def restaurant_ratings(filename):

    file_name = open(filename)
    restaurant_list = {}
    new_restaurant_name, new_restaurant_rating = get_new_restaurant_rating()
    restaurant_list[new_restaurant_name] = new_restaurant_rating

    for line in file_name:
        # words = line.split(":")
        # restaurant = words[0]
        # rating = words[1]
        # rating = rating[0:1]
        restaurant, rating = line.split(':')
        restaurant_list[restaurant] = int(rating)

    for restaurant_name in sorted(restaurant_list):
        print(f"{restaurant_name} is rated at {restaurant_list[restaurant_name]}.")


def get_new_restaurant_rating():
    new_restaurant_name = input("Enter the name of the restaurant: ")
    new_restaurant_rating = int(input("Enter the rating restaurant: "))
    return new_restaurant_name, new_restaurant_rating


restaurant_ratings('scores.txt')
