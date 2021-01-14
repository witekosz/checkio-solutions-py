import re


def is_stressful(subj: str) -> bool:
    """
        recognise stressful subject
    """
    print(subj)
    # is_st = "help" in subj.lower()
    is_st = re.search("[help]", subj.lower())
    print(is_st)
    return bool(is_st)


if __name__ == '__main__':
    is_stressful("h!e!l!p")
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
