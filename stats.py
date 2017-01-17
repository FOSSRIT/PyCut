import pstats

p = pstats.Stats("output.txt")
p.sort_stats("time").print_stats(25)