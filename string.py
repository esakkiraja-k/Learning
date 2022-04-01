def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams

    Args:
       str1(string),str2(string): Strings to be checked if they are anagrams
    Returns:
       bool: If strings are anagrams or not
    """

    if len(str1) != len(str2):
        # Clean strings
        str1 = str1.replace(" ", "").lower()
        str2 = str2.replace(" ", "").lower()

    if sorted(str1) == sorted(str2):
       return True

    return False

print("pass" if anagram_checker('test','test') else "fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")


