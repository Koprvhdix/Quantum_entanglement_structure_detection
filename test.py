# import copy
#
#
# def recursion_mini_cover_list(pair_set_cover_dict, need_cover_set, mini_count):
#     cover_list = list()
#     sorted_keys_dict = dict()
#     for key in pair_set_cover_dict:
#         if pair_set_cover_dict[key] & need_cover_set == need_cover_set:
#             cover_list.append([key])
#         elif len(pair_set_cover_dict[key] & need_cover_set) > 0:
#             sorted_keys_dict[key] = len(pair_set_cover_dict[key] & need_cover_set)
#
#     if len(cover_list) > 0 or mini_count == 1:
#         return cover_list
#
#     sorted_keys = [k for k, v in sorted(sorted_keys_dict.items(), key=lambda item: item[1], reverse=True)]
#     temp_pair_set_cover_dict = copy.deepcopy(pair_set_cover_dict)
#     for key in sorted_keys:
#         next_need_cover_set = need_cover_set - pair_set_cover_dict[key]
#         del temp_pair_set_cover_dict[key]
#         current_cover_list = recursion_mini_cover_list(temp_pair_set_cover_dict, next_need_cover_set, mini_count - 1)
#         if len(current_cover_list) > 0:
#             if len(current_cover_list[0]) + 1 < mini_count:
#                 mini_count = len(current_cover_list[0]) + 1
#                 cover_list.clear()
#                 cover_list.extend([cover_item + [key] for cover_item in current_cover_list])
#             elif len(current_cover_list[0]) + 1 == mini_count:
#                 cover_list.extend([cover_item + [key] for cover_item in current_cover_list])
#
#     return cover_list
#
#
# if __name__ == "__main__":
#     print(recursion_mini_cover_list({'0001.0010': {2, 4}, '0001.0100': {1, 2, 3}}, {1, 2, 3, 4}, float('inf')))
