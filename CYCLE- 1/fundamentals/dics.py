
def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"Firstname": "Edier", "Lasname": "Gama"}

    super_list = [
         {"Firstname": "Edier", "Lastname": "Gama"},
         {"Firstname": "Luis", "Lastname": "Torres"},
         {"Firstname": "Luisa", "Lastname": "Fajardo"},
         {"Firstname": "Juan", "Lastname": "Calderon"},
         {"Firstname": "Camila", "Lastname": "Gama"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums":[1.1, 4.5, 6.6]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

 

if __name__ == "__main__":
    run()