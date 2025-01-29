import emoji

def main():
    # Prompt for input from the user or test case
    i = input()

    # Convert the emoji alias to the actual emoji and print it
    # Example: ":1st_place_medal:" -> 🥇
    print(emoji.emojize(i, language='alias'))


# Call the main function
main()
