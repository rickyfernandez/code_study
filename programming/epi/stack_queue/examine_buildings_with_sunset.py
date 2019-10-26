
def examine_buildings_with_sunset(heights):
    stack = []
    for i, height in enumerate(heights):
        while stack and height >= stack[-1][1]:
            stack.pop()
        stack.append((i,height))
    return [val[0] for val in stack]

if __name__ == "__main__":
    build = [2, 4, 1, 7, 5, 2]
    print(f"Buildings east-west: {build} buildings that see the sunset {examine_buildings_with_sunset(build)}")
