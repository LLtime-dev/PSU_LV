
numbers = []

while True:
    user_input = input("Unesite broj ili 'Done' za kraj: ")

    if user_input.lower() == "done":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Pogrešan unos! Molimo unesite broj ili 'Done'.")

    if numbers:
        count = len(numbers)
        average = sum(numbers) / count
        minimum = min(numbers)
        maximum = max(numbers)
        sorted_numbers = sorted(numbers)

        print(f"Unijeli ste {count} brojeva.")
        print(f"Srednja vrijednost: {average}")
        print(f"Minimalna vrijednost: {minimum}")
        print(f"Maksimalna vrijednost: {maximum}")
        print(f"Sortirana lista: {sorted_numbers}")
    else:
        print("Niste unijeli niti jedan broj.")

