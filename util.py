def getIntInput(prompt, options):
    print()
    while True:
        response = input(prompt + " (Options: " + ", ".join(options) + "): ")
        if response not in options:
            print("Error: Invalid option: " + response)
            continue
        break
    return int(response)
