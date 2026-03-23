from operator import ne

capitals = {
    "France": "Paris",
    "China": "Beijing",
}

# travel_log = {
#     "China": ["Shanghai","Beijing","Guangzhou"],
# }

print(travel_log["China"][0])

nested_list = ["A","B",["C","D"]]
print(nested_list[2][0])


travel_log = {
    "China": {
        "num_times_visited": 8,
        "cities_visited": ["Shanghai","Beijing","Chengdu"]
    },
}
