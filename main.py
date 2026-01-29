source = [3, 2, 1]
auxiliary = []
target = []
move_count = 0


def towers_of_hanoi(source, auxiliary, target, num_disks):
    """Move `num_disks` from `source` to `target` using `auxiliary`.

    Returns the total number of moves performed (updates global move_count).
    """

    state = {
        "source": source,
        "auxiliary": auxiliary,
        "target": target,
        "num_disks": num_disks,
    }

    print(state)

    global move_count
    if num_disks == 1:
        disk = source.pop()
        target.append(disk)
        move_count += 1
    else:
        towers_of_hanoi(source, target, auxiliary, num_disks - 1)
        towers_of_hanoi(source, auxiliary, target, 1)
        towers_of_hanoi(auxiliary, source, target, num_disks - 1)

    print({"move_count": move_count})
    return move_count


print(towers_of_hanoi(source, auxiliary, target, len(source)))
