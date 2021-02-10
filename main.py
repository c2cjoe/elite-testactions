#!/usr/bin/env python3

# query/response pairs as tuples
queries = [
    ("bye", "Goodbye"),
    ("hello", "Hello, how are you!"),
    ("what is your name", "My name is chatbot.")
    ]

# given an input query string, return a response
def decide_response(query):
    # iterate through all the known queries
    for q in queries:
        if q[0] == query:
            return q[1]
    return "I didn't understand that"

def main():
    print("Hello, I am the chatbot")
    while True:
        user_input = input()
        response = decide_response(user_input)
        print(response)
        # exit program if user says "bye"
        if response == "Goodbye":
            break

if __name__ == "__main__":
    main()
