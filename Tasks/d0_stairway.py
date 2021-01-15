from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    if len(stairway) == 0:
        return None
    min_list = []
    for i in range(len(stairway)):
        if i != 0 and i != 1:
            option = stairway[i] + min(min_list[i - 2], min_list[i - 1])
            min_list.append(option)
        else:
            min_list.append(stairway[i])
    return min_list[-1]
