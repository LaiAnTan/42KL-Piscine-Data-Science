ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# list is mutable
ft_list[1] = "World!"

# tuple is immutable
temp = list(ft_tuple)
temp[1] = "Malaysia!"
ft_tuple = tuple(temp)

# set is unordered
ft_set.discard("tutu!")
ft_set.add("Kuala Lumpur!")

# dict
ft_dict["Hello"] = "42KL!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
