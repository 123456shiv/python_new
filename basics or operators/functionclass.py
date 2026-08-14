def course_price(course):
    if course == "Python":
        price = 500000
        discount = 13

    elif course == "Web Development":
        price = 600000
        discount = 13

    elif course == "Data Science":
        price = 800000
        discount = 13

    else:
        return "Course not available"

    discount_amount = price * discount / 100
    final_price = price - discount_amount

    return price, discount_amount, final_price


course = input("Enter course: ")

price, discount_amount, final_price = course_price(course)

print("Base Price:", price)
print("Discount:", discount_amount)
print("Final Price:", final_price)