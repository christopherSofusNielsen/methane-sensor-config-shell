

def show_menu(options):
    for index, opt in enumerate(options):
        print(f"[{index}] {opt}")

    return show_select(len(options))


def show_select(length):
    sel = input(f"Select menu [0..{length}]: ")
    try:
        if(sel.lower() == "q" or sel.lower() == "exit"):
            return None
        index = int(sel)
    except ValueError:
        print("use a number or q/exit to quit program")
        return show_select(length)

    if(not (0 <= index < length)):
        print("Not a valid input, try again...")
        return show_select(length)

    return index
