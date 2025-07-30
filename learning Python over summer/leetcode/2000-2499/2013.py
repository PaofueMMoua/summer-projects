class DetectSquares:

    def __init__(self):
        self.points = collections.defaultdict(int)
        # you get the self
        # get the points and set it equal to the collections with a dictionary of integers 

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        # take the points list and make it a list of tuples to make it hashable and add one 

    def count(self, point: List[int]) -> int:
        square_count = 0
        x1, y1 = point
        # set a variable called something count
        # set new variables equal to point so then you can work easier  

        for (x2, y2), n in self.points.items():
            x_dist, y_dist = abs(x1 - x2), abs(y1 - y2)
            if x_dist == y_dist and x_dist > 0:
                corner1 = (x1, y2)
                corner2 = (x2, y1)
                if corner1 in self.points and corner2 in self.points:
                    square_count += n * self.points[corner1] * self.points[corner2]
        return square_count
    # make a for loop that iterates for the tuple and unpacks them while it checks if its in the points
    # get the abolute distance between the two points
    # check if the distance x is equal to the distance y and that the distance of x is greater than 0
    # next set two more variables to the coordinates
    # check if the corner1 in the points and corner 2 in the points then
    # you take the count from earlier and set it equal to itself plus n * self.points[corner1] times self.points[corner2]
    # then return square count outside of the for loop 

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)