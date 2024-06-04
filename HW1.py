# Problem 1
def hello(input_string):
    return f"Hello {input_string}, my name is Jesmyn."

if __name__ == "__main__":
    pass  

# Problem 2
def divisible(n):
    return [i for i in range(0, 10001) if i % n == 0]

if __name__ == "__main__":
    pass  

# Problem 3
def remove_none(input_dict):
    return {a: b for a, b in input_dict.items() if b is not None}

if __name__ == "__main__":
    pass  

# Problem 4
def length(input_list):
    length = 0
    for _ in input_list:
        length += 1
    return length

if __name__ == "__main__":
    pass  

# Problem 5
def my_reverse(input_list):
    reversed_list = []
    for item in input_list:
        reversed_list.insert(0, item)
    return reversed_list

if __name__ == "__main__":
    pass  

# Problem 6
def my_min(input_list):
    if not input_list:
        return None  
    min_element = input_list[0]
    for item in input_list:
        if item < min_element:
            min_element = item
    return min_element

if __name__ == "__main__":
    pass  

# Problem 7
def written_numbers(n):
    if n < 0 or n > 999:
        return "Input must be between 0 and 999."

    # Dic for numbers
    number_words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
        80: "eighty", 90: "ninety"
    }

    def number_to_words(num):
        if num <= 20:
            return number_words[num]
        elif num < 100:
            tens, below_ten = divmod(num, 10)
            return number_words[tens * 10] + ("" if below_ten == 0 else " " + number_words[below_ten])
        else:
            hundreds, below_hundred = divmod(num, 100)
            return number_words[hundreds] + " hundred" + ("" if below_hundred == 0 else " " + number_to_words(below_hundred))

    return {i: number_to_words(i) for i in range(n + 1)}

if __name__ == "__main__":
    pass  

# Problem 8
def fizzbuzz(n):
    output = ""
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            output += "fizzbuzz\n"
        elif i % 3 == 0:
            output += "fizz\n"
        elif i % 5 == 0:
            output += "buzz\n"
        else:
            output += "\n"
    return output

if __name__ == "__main__":
    pass  
    
    #should testing
    
