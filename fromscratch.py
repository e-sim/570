import sys
import collections
import re

#read in morph rules FST
#make a method that expands a single edge
# it takes an input word and an edge object (the latter matches output)


class Edge:

    def __init__(self, in_word, dest, output):
        self.in_word = in_word
        self.dest = dest
        self.output = output

class Node:

    def __init__(self, name):
        self.name = name
        self.adjacents = []
        self.accept = False

    #for testing
    def __repr__(self):
        return "name=" + self.name + " accept=" + str(self.accept)
               # + " (" + str(self.adjacents) + ")"

    def set_accept(self):
        self.accept = True


#### debug print
DEBUGGING = False
def debug_print(text):
    if DEBUGGING:
        print(text)
        sys.stdout.flush()


#this edge should already match the output when it's called
#origin is a Node, edge is an Edge
#return the number counter's on
def expand_edge(word, origin, edge, counter):
    curr_node = origin
    for letter in word[0:len(word) - 1]:
        node_name = str(counter)
        next_node = Node(node_name)
        eps = "*e*"
        node_dict[node_name] = next_node
        new_edge = Edge(letter, node_name, eps)
        node_dict[curr_node].adjacents.append(new_edge)
        counter += 1
        curr_node = next_node
    letter = word[len(word) - 1]
    new_edge = Edge(letter, edge.dest, edge.output)
    node_dict[curr_node].adjacents.append(new_edge)
    counter += 1
    return counter



FST_FILE = open(sys.argv[2], "r")
node_dict = collections.OrderedDict()

for line in FST_FILE:
    line = line.rstrip()

    #regex for each line of fst file
    FST_ACCEPT_REGEX_PATTERN = re.compile(r"(\w+)$")
    FST_EDGE_REGEX_PATTERN = re.compile(r"\((\w+) \((\w+) \"(\w*)\" +\"(\w*)\" (\d(\.\d+))?\)\)")
    accept_match = FST_ACCEPT_REGEX_PATTERN.match(line)

    if accept_match:
        acc_state = accept_match.group(1)

    else:
        edge_match = FST_EDGE_REGEX_PATTERN.match(line)

        curr = edge_match.group(1)
        next_node_code = edge_match.group(2)
        in_word = edge_match.group(3)
        out_word = edge_match.group(4)
        num_nodes = 0

        if curr not in node_dict:

            new_node = Node(curr)
            num_nodes += 1
            node_dict[curr] = new_node
            
            if acc_state == curr:
                new_node.set_accept()

            debug_print("made " + str(new_node))

        #turns out you gotta make sure all destination nodes are made too
        if next_node_code not in node_dict:

            new_node = Node(next_node_code)
            num_nodes += 1
            node_dict[next_node_code] = new_node
            
            if acc_state == next_node_code:
                new_node.set_accept()

            debug_print("made " + str(new_node))


        new_edge = Edge(in_word, next_node_code, out_word)
        node_dict[curr].adjacents.append(new_edge)


FST_FILE.close()

# start output stuff
