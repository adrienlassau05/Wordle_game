def total_progress(progress_list, guess_list):
    for i, ch in enumerate(progress_list):
        print(ch, " ", end="")
        print(guess_list[i])


progress_list = ["🟨⬛⬛⬛⬛","⬛🟩🟨⬛🟩", "⬛🟩🟩🟩🟩"]
guess_list = ["adieu", "plant", "gloat"]
total_progress(progress_list, guess_list)
