from collections import namedtuple


with open("day12.txt") as file:
    data_list = file.readlines()


with open("day12_test.txt") as file:
    test_data_list = file.readlines()

print(test_data_list)

Node_info = namedtuple("Node_info", "node spokes")

# my_node = Node_info(2, [0, 3])


def process_str(data_str: str):
    list_str = data_str.strip().replace("<->", ",").split(",")
    list_ints = [int(num.strip()) for num in list_str]
    if len(list_ints) < 2:
        raise TypeError("Not a valid node")
    return Node_info(list_ints[0], set(list_ints[1:]))


assert process_str("1825 <-> 608, 839, 876, 1965\n") == Node_info(
    1825, {608, 839, 876, 1965}
)

test_data_node = [process_str(data) for data in test_data_list]
data_node = [process_str(data) for data in data_list]


print(test_data_node)


def connected_nodes(test_data, node=0):
    """Returns all the nodes conneted to node=0"""
    nodes = {}
    newnodes = {node}
    while nodes != newnodes:
        # stops when a pass procduces no new nodes
        nodes = newnodes
        for node_info in test_data:
            # search the graph and add any new nodes from node or spokes to newnodes
            if node_info.node in newnodes:
                newnodes = newnodes.union(node_info.spokes)
            if set(node_info.spokes).intersection(newnodes) != set():
                # pass
                # print(node_info.node, newnodes)

                newnodes = newnodes.union({node_info.node})
    return newnodes


print(
    f"0 is connected to {len(connected_nodes(test_data_node))} other nodes in the test data. "
)

print(f"0 is connected to {len(connected_nodes(data_node))} other nodes. ")


def number_of_groups(test_data):
    """"""
    listofnodes = set()
    for data in test_data:
        listofnodes.add(data.node)
        listofnodes = listofnodes.union(data.spokes)

    print("list of all nodes:", listofnodes)
    groups = []
    while listofnodes:
        # removes a connected group from listofnodes every loop
        group = connected_nodes(test_data, list(listofnodes)[0])
        groups.append(group)
        for point in group:
            # print(listofnodes)
            listofnodes.remove(point)
        print(group)
    return len(groups)


print("The number of groups in the test set is", number_of_groups(test_data_node))

print("The number of groups is", number_of_groups(data_node))
