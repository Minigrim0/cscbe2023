# Import beautifulsoup4
from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = "http://54.78.74.244/"
# Get the HTML from the URL
html = requests.get(url).text
# Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Get all lists
lists = soup.find_all("ul")
# Iterate through the lists and get all elements

outliers = [
    "Elephant", "Chair", "City", "Butterfly", "sun", "telephone",
    "ocean", "giraffe", "tree", "Horse", "circus", "train",
    "computer", "moon", "zoo", "house", "rock", "office"]
outliers = [elem.lower() for elem in outliers]

correct = [
    'BBQ Sauce',
    "salmon",
    'Bacon',
    'Basil',
    'Beef',
    'Bell Peppers',
    'Bread',
    'Broccoli',
    'Butter',
    'Caesar Dressing',
    'Cannellini Beans',
    'Carrots',
    'Celery',
    'Cheese',
    'Chicken Breasts',
    'Chicken Broth',
    'Chicken Pieces',
    'Clams',
    'Croutons',
    'Eggs',
    'Flour',
    'Flour Tortillas',
    'Garden',
    'Garlic',
    'Ground Beef',
    'Heavy Cream',
    'Ketchup',
    'Kidney Beans',
    'Lemon',
    'Lettuce',
    'Lobster',
    'Macaroni',
    'Marinara Sauce',
    'Mayonnaise',
    'Milk',
    'Mozzarella Cheese',
    'Mushrooms',
    'Noodles',
    'Olive Oil',
    'Onion',
    'Onions',
    'Pancetta',
    'Parmesan Cheese',
    'Pasta',
    'Peas',
    'Pepper',
    'Pork Chops',
    'Pork Ribs',
    'Potatoes',
    'Red Wine',
    'Rice',
    'Romaine Lettuce',
    'Salt',
    'Shrimp',
    'Soy Sauce',
    'Spaghetti',
    'Steak',
    'Sugar',
    'Sugar, Vanilla Extract',
    'Tacos Shells',
    'Tomato',
    'Tomato Sauce',
    'Tomatoes',
    'Tuna',
    'Turkey',
    'Vegetables',
    'Vinegar',
    'White Wine',
    'Ziti',
]
correct = [elem.lower() for elem in correct]

current_outliers = []

element_dict = {}
for list in lists:
    elements = list.find_all("li")
    # Iterate through the elements and print the text
    for i, element in enumerate(elements):
        # Print first element
        if (element.text.lower() in outliers) or (element.text.lower() not in correct):
            print(i, element.text)
            current_outliers.append(element.text)
        if element.text in element_dict:
            element_dict[element.text] += 1
        else:
            element_dict[element.text] = 1

# Print the elements
# print(element_dict)
# print(len(element_dict))
# for element in sorted(element_dict, key=lambda x: element_dict[x], reverse=True):
#     print(f"{element}({element_dict[element]})", end=", ")

# Find outliers

# for element in element_dict:
#     if element_dict[element] == 1:
#         print(element)

rep = requests.post(
    url,
    data={
        "in1": current_outliers[0],
        "in2": current_outliers[1],
        "in3": current_outliers[2],
        "in4": current_outliers[3],
    })
print(rep.content)
