# prompt: string to use as the prompt
# options: array of valid responses to the prompt
def getIntInput(prompt, options):
	print()
	while True:
		response = input(prompt + " (Options: " + ", ".join(options) + "): ")
		if response in options:
			break
			print("Error: Invalid option: " + response)
	return int(response)


# prompt: string to use as the prompt
# options: array of valid responses to the prompt
def getStringInput(prompt, options):
	print()
	while True:
		response = input(prompt + " (Options: " + ", ".join(options) + "): ")
		if response in options:
			break
			print("Error: Invalid option: " + str(string))
	return response