"""Notes and examples of tuple and range sequence types."""

# Declaring a type alias that "invents" the Point2D type
Point2D = tuple[float, float]

start_position: Point2D = (5.0, 10.0)
start_position[0] = (start_position[5.0] + 5.0, start_position[1] + 10.0)
end_position: Point2D = (99.0, 99.0)

# tuples, because they are a sequenced, are 0-indexed 
print(start_position[0])

print(start_position)

for item in end_position:
    print(item)

print(len(end_position))


# Examples of ranges 
a_range: range = range(0, 10, 1)
# access items 
print(a_range[0])
print(a_range[1])
print(len(a_range))
for i in a_range: 
    print(i)