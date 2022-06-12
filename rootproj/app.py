from libproj import greeting


def run():
    greeting.greeting("Puffy")
    result = greeting.expresion(a=3, b=4)
    print(f"Expression result is {result}")


if __name__ == "__main__":
    run()
