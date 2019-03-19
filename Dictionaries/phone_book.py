
phone_book = {}


def add(phone_number, name):

    if name in phone_book:
        phone_book[name] = phone_book[name] + [phone_number]
    else:
        phone_book[name] = [phone_number]


def delete(name):

    if name in phone_book:
        phone_book.pop(name)


def find(name):
    if name in phone_book:
        numbers = phone_book[name]
        print(min(numbers))
    else:
        print("not found")


add(123456, "JACK")
add(12345678, "JACK")
add(1111, "jack")

delete("jackeee")

find("JACK")
find("jackee")

print(phone_book)