

def mergeTwoLists(list1, list2):
    # Covering empty list edges
    if not list1 and not list2:
        return []
    elif not list1 and list2:
        return list2
    elif not list2 and list1:
        return list1

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None
            self.tail = None

    two_mergedLL = LinkedList()

    two_merged = []

    if len(list1) > len(list2):
        large = list1
        small = list2
        extension = large[len(large) - len(small): len(large)]
    elif len(list1) < len(list2):
        large = list2
        small = list1
        extension = large[len(large) - len(small): len(large)]
    else:  # len ==
        large = list1
        small = list2
        extension = []

    i = 0
    while i < len(small):
        if large[i] < small[i]:
            two_merged.append(large[i])
            two_merged.append(small[i])
        else:
            two_merged.append(small[i])
            two_merged.append(large[i])
        i += 1

    two_merged.extend(extension)
    return two_merged


list1 = [0, 1, 2, 4, 6, 7]
list2 = [1, 3, 4]
print(mergeTwoLists(list1, list2))

# if not list1 and not list2:
#     return []
# elif not list1 and list2:
#     return list2
# elif not list2 and list1:
#     return list1
#
# two_merged = []
#
# # if len(list1) > len(list2):
# #     large = list1
# #     small = list2
# #     extension = large[len(large) - len(small): len(large)]
# # elif len(list1) < len(list2):
# #     large = list2
# #     small = list1
# #     extension = large[len(large) - len(small): len(large)]
# # else:  # len ==
# #     large = list1
# #     small = list2
# #     extension = []
# #
# # i = 0
# # while i < len(small):
# #     if large[i] < small[i]:
# #         two_merged.append(large[i])
# #         two_merged.append(small[i])
# #     else:
# #         two_merged.append(small[i])
# #         two_merged.append(large[i])
# #     i += 1
# #
# # two_merged.extend(extension)
# # return two_merged