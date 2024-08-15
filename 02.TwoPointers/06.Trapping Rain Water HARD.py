def f(height):
    def get_middle_water(l, r, pre_l, pre_r):
        if l + 1 >= r:  # base case
            return 0

        # calculates the most water between two bars
        max_water_dict = {'left_i': l, 'right_i': r, 'water': 0}
        while l < r:
            cur_water = (r - l - 1) * min(height[r], height[l])  # ! -1
            if cur_water > max_water_dict['water']:
                max_water_dict['left_i'] = l
                max_water_dict['right_i'] = r
                max_water_dict['water'] = cur_water

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        # now remove the bars in between
        l, r = max_water_dict['left_i'] + 1, max_water_dict['right_i']
        middle = max_water_dict['water']
        lower_bar = min(
            height[max_water_dict['left_i']],
            height[max_water_dict['right_i']]
        )
        while l < r:
            if height[l] > lower_bar:
                middle -= lower_bar
            else:
                middle -= height[l]
            l += 1

        max_water_dict['water'] = middle

        left = get_middle_water(0, max_water_dict['left_i'])
        right = get_middle_water(max_water_dict['right_i'], len(height) - 1)
        res = left + middle + right
        return res

    res = get_middle_water(0, len(height) - 1)
    return res


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(f(arr))
