class TreeNode(object):

    def __init__(node, degree):

        node.degree = degree
        node.bottomLevel = True

        node.travelNodes = []
        node.prices = []

    def full_node(node):

        if node.degree == len(node.travelNodes):
            return True
        else:
            return False

    def display_test(node):

        if not node.bottomLevel:
            for price in node.prices:
                price.display_test()

        else:
            for price in node.travelNodes:
                print("price: ", price[0], "date: ", price[1])

    def get_price_node(node, final_prices):

        if not node.bottomLevel:
            for price in node.prices:
                price.get_price_node(final_prices)

        else:
            for price in node.travelNodes:
                final_prices.append((price[0], price[1]))



    def get_average(node, sum):

        if not node.bottomLevel:
            for price in node.prices:
                price.get_average(sum)
        else:
            for price in node.travelNodes:
                sum[0] += price[0]
                sum[1] += 1

    def get_minimum(node, min):

        if not node.bottomLevel:
            node.prices[0].get_minimum(min)
        else:
            min[0] = node.travelNodes[0][0]

    def get_maximum(node, max):

        if not node.bottomLevel:
            node.prices[len(node.prices)-1].get_maximum(max)
        else:
            max[0] = node.travelNodes[len(node.travelNodes)-1][0]


    def insertNode(node, price):

        if len(node.travelNodes) == 0:
            node.travelNodes.append(price)
            node.prices.append(price)
            return

        for x, travelNode in enumerate(node.travelNodes):

            if price[0] <= travelNode[0]:
                node.travelNodes = node.travelNodes[:x] + [price] + node.travelNodes[x:]
                node.prices = node.prices[:x] + [price] + node.prices[x:]
                break

            elif x == len(node.travelNodes)-1:
                node.travelNodes.append(price)
                node.prices.append(price)
                break

    def break_node(node):

        node.bottomLevel = False

        left_node = TreeNode(node.degree)
        right_node = TreeNode(node.degree)

        middle_index = node.degree // 2

        left_node.travelNodes = node.travelNodes[:middle_index]
        right_node.travelNodes = node.travelNodes[middle_index:]

        left_node.prices = node.prices[:middle_index]
        right_node.prices = node.prices[middle_index:]

        new_key = right_node.travelNodes[0]
        node.travelNodes = [new_key]
        node.prices = [left_node, right_node]

class BPlusTree(object):

    def __init__(tree, prices, degree=4):
        tree.root_node = TreeNode(degree)
        tree.constructor(prices)

    def constructor(tree, prices):

        for item in prices:
            tree.insert_tree_node(item)


    def insert_tree_node(tree, price):

        temp_parent = None
        temp_child = tree.root_node

        while not temp_child.bottomLevel:
            temp_parent = temp_child
            temp_child, index = tree.search(temp_child, price)

        temp_child.insertNode(price)
        full = temp_child.full_node()

        if full:
            temp_child.break_node()

            if temp_parent != None and not temp_parent.full_node():
                tree.combine_node(temp_parent, temp_child, index)

    def display_tree(tree):
        tree.root_node.display_test()


    def get_prices(tree):
        final_prices = []
        tree.root_node.get_price_node(final_prices)
        return final_prices

    def search(tree, node, price):

        smaller = False
        child_node = 0
        index = 0

        for x, temp_node in enumerate(node.travelNodes):
            if price[0] < temp_node[0]:
                smaller = True
                child_node, index = node.prices[x], x
                break

        if smaller:
            return child_node, index
        else:
            return node.prices[x+1], x+1


    def get_average_price(tree):

        sum = [0, 0]
        tree.root_node.get_average(sum)
        return sum[0] / sum[1]


    def get_minimum_price(tree):

        min = [0]
        tree.root_node.get_minimum(min)
        return min[0]

    def get_maximum_price(tree):

        max = [0]
        tree.root_node.get_maximum(max)
        return max[0]


    def combine_node(tree, parent_node, child_node, index):

        parent_node.prices.pop(index)
        new_parent = child_node.travelNodes[0]

        for x, price in enumerate(parent_node.travelNodes):

            if x == len(parent_node.travelNodes)-1:
                parent_node.travelNodes = parent_node.travelNodes + [new_parent]
                parent_node.prices = parent_node.prices + child_node.prices
                break

            if new_parent[0] < price[0]:
                parent_node.travelNodes = parent_node.travelNodes[:x] + [new_parent] + parent_node.travelNodes[x:]
                parent_node.prices = parent_node.prices[:x] +  child_node.prices + parent_node.prices[x:]
                break


'''if __name__ == '__main__':

    prices = [(34263.36638073, 20210706), (33963.88270598, 20210707), (32872.58702223, 20210708),
              (33786.36327715, 20210709), (33558.33135714, 20210710), (34247.71823295, 20210711),
              (33124.12797663, 20210712), (32787.53270551, 20210713), (32809.44997193, 20210714),
              (31889.78060343, 20210715)]

    bplustree = BPlusTree(prices)

    print("")
    print("Current tree (Sorted by increasing price: ")
    print("")
    bplustree.display_tree()
    print("")

    total = bplustree.get_average_price()
    print("average price: ", total)

    min = bplustree.get_minimum_price()
    print("minimum price: ", min)

    max = bplustree.get_maximum_price()
    print("maximum price: ", max)

    list = bplustree.get_prices()
    print("")
    print("test printing out fist item: ", list[0][0])'''























