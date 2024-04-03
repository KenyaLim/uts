import random

def generate_random_number(lower_limit, upper_limit):
    return random.randint(lower_limit, upper_limit)

def get_user_guess():
    while True:
        try:
            guess = int(input("Masukkan tebakan anda (1 s.d 1000): "))
            if guess >= 1 and guess <= 1000:
                return guess
            else:
                print("Tebakan harus berada dalam rentang 1 s.d 1000")
        except ValueError:
            print("Tebakan harus berupa angka")

def compare_guesses(user_guess, random_number):
    if user_guess == random_number:
        return "Jawaban anda benar"
    elif user_guess > random_number:
        return "Terlalu besar"
    else:
        return "Terlalu kecil"

def play_game():
    random_number = generate_random_number(1, 1000)
    attempts = 10
    score = 0

    while attempts > 0:
        user_guess = get_user_guess()
        feedback = compare_guesses(user_guess, random_number)
        print(feedback)

        if feedback == "Jawaban anda benar":
            score = attempts * 100
            break

        attempts -= 1

    return score

def main():
    print("Selamat datang di permainan tebak angka!")
    print("Anda dibatasi hanya bisa menebak maksimal 10 kali.")
    print("Scoreanda adalah sisa kesempatan * 100.")

    score = play_game()
    print(f"Game selesai. Nilai anda adalah {score}.")

if __name__ == "__main__":
    main()