def mark_intervals(plot, interval,fun):
    for (start, end) in interval:
        plot.scatter(end,fun(start), marker="|", linewidths=2, c='green')
        plot.scatter(end,fun(end), marker="|", linewidths=2, c='green')