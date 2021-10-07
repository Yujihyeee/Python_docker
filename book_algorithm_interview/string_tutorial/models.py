class Palindrome(object):

    def str_to_list(payload: str) -> []:
        ''' strs = []
            for char in payload:
                if char.isalnum():
                    strs.append(char.lower())

            return strs'''
        return [i for i in payload if i.isalnum()]

    def isPalindrome(ls: []) -> bool:
        return {"RESULT": True for i in ls if ls.pop(0) != ls.pop()}

    ls = str_to_list("A man, a plan, a canal: Panama")
    print(ls)
    isPal = isPalindrome(ls)
    print(isPal["RESULT"])


class Reverse(object):
    def str_to_list(payload: str) -> []:
        return

    def reverse_List(ls: []) -> []:
        return []

    def List_to_str(ls: []) -> str:
        return ''