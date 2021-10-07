from book_algorithm_interview.string_tutorial.models import Reverse

if __name__ == '__main__':
    ls = Reverse().str_to_list(input("Input: "))
    reversed_ls = Reverse().reverse_List(ls)
    print(Reverse().List_to_str(reversed_ls))
