def minTimeToVisitAllPoints(points):
    time = 0

    for i in range(1, len(points)):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        print(dx,"dx", dy, "dy")

        time += max(dx, dy)

    return time

result = minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
print(result)