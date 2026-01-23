str = "Camus"

print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])

name = input("Enter your name: ")
Country = input("Enter where you from: ")

print(f"Hey my name is {name} and I am from {Country}.")

str1 = "aldous Huxley was born in 1894."
str1 = str1[0].upper() + str1[1:]

print(str1)

str2 = "Where now? Who now? When now?"

str2_split = str2[0:10]

str2_split1 = str2[11:19]

str2_split2 = str2[20:]


list = [str2_split, str2_split1, str2_split2]

print(list)

words = ["The", "fox", "jumped", "over", "the", "fence", "."]

print(" ".join(words))

replace = "A screaming cat comes across the sky."
print(replace.replace("s", "$"))

var = "three three three"
var1 = " three "
print(var1 * 3)
