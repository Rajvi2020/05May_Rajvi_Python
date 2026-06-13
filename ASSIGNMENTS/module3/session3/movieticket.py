def book_movie_ticket(balance):
    try:
        tickets = int(input("Enter number of tickets: "))

        price_per_ticket = balance / tickets
        print("Price per ticket:", price_per_ticket)

    except ZeroDivisionError:
        print("Error: Tickets cannot be zero!")
    except ValueError:
        print("Error: Please enter valid number!")

book_movie_ticket(999)