#varun yelchur
def encoder(password):
    final_list = []
    temp_list = list(password.strip(" "))
    for i in temp_list:
        i = int(i)
        i += 3
        i = str(i)
        final_list.append(i)
    password = str(''.join(final_list))
    return password

def main():
    condition = True
    while condition:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            enc = encoder(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif user_input == 2:
        # print(f"The encoded password is {enc}, and the original password is {decoder(enc)}.")
        elif user_input == 3:
            break


if __name__ == "__main__":
    main()