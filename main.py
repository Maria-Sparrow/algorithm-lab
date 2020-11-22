from in_out import write_result, read_pairs
from utils import wedding_func

if __name__ == '__main__':
    # graph = [(1, 2), (2, 4), (3, 5)]
    graph = []
    in_file = "wedd.in"
    out_file = "wedding_result.out"
    graph = read_pairs(in_file, graph)
    graph_length = len(graph)

    print("Pairs: " + str(len(graph)) + "Result:")
    how_many_pairs = wedding_func(graph, graph_length)
    write_result(out_file, how_many_pairs)
    print(how_many_pairs)
