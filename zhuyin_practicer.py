import json
import os
from score_keeper import ScoreKeeper
from zhuyin_type import ZhuyinType


game_score = ScoreKeeper()

def get_number():
    while True:
        try: 
            number = int(input("Enter your choice [1-4]: "))
            if 1 <= number <= 4:
                return number
            else:
                print("Please enter a value of 1-4")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def run_questions(question_dict):

    
    
    # Extract the different parts
    question = question_dict["question"]
    # print(question_dict["question"])

    options = question_dict["options"]
    # print(question_dict["options"])


    # Ask the question
    print(f"Correct Zhuyin for: {question} ?")
    for i in range(0, len(options)):
        print(f"{i+1}: {options[i]}")
    chosen_number = get_number()


    # Get the answer
    answer = question_dict["answer"]
    # print(question_dict["answer"])

    if chosen_number == answer:
        print("Correct!\n")
        game_score.add_to_correct()
    else:
        print("Incorrect\n")

    print(game_score)

    # print(f"{question} ?")
    # print(f"{options} ?")


def load_zhuyin_json_list(zhuyin_type):

    '''Returns a list of the argument type (from enum)'''

    consonant_list = []
    vowel_list = []
    all_list = []
    file_path = os.path.join(os.getcwd(), 'zhuyin.json')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Get the consonants
            consonant_list = data["consonants"]
    
            # Get the vowels
            vowel_list = data["vowels"]

            #Get everything
            all_list = consonant_list + vowel_list

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please check the JSON format.")

    # Return the type that is being passed as an argument
    # if zhuyin_type is ZhuyinType.CONSONANT:
    #     return consonant_list
    # elif zhuyin_type is ZhuyinType.VOWEL:
    #     return vowel_list
    # elif zhuyin_type is ZhuyinType.ALL:
    #     return all_list
    # else:
    #     return f"Incorrect Argument provided: {zhuyin_type}"

    if zhuyin_type == "consonant":
        return consonant_list
    elif zhuyin_type == "vowel":
        return vowel_list
    elif zhuyin_type == "all":
        return all_list
    else:
        return all_list



def main():


    # If doing the score here:
    # total_questions_amount = len(consonant_list) + len(vowel_list)
    # game_score = ScoreKeeper(total_questions_amount)
    # list_to_practice = load_zhuyin_json(ZhuyinType.ALL)
    list_to_practice = load_zhuyin_json_list("all")


    # Add the list here, or abstract it away later
    game_score.add_to_total(len(list_to_practice))

    for i in list_to_practice:
        # print(i)
        run_questions(i)

    # Print the results:
    final_percentage = game_score.correct / game_score.total * 100
    print(f"\nFinal Outcome: {final_percentage:.1f}%")


    return

if __name__ == '__main__':
    main()
