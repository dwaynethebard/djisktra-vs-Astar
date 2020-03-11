from priorityQueue import PriorityQueue
from math import sqrt


class PathFind:
    def __init__(self, vertices=[]):
        self.vertices = vertices

    def djisktra(self, a, b):
        distances = [float("inf") for _ in self.vertices]
        distances[a] = 0
        predecessors = [None for _ in self.vertices]
        # queue = PriorityQueue()
        queue = PriorityQueue()
        queue.enqueue((distances[a], self.vertices[a].label))

        while True:
            if queue.empty():
                break
            # print(queue)
            _, current = queue.dequeue()
            if current is b:
                break
            # dequeue a node we already looked at
            # this may not be necessary because it will just not decrease any travel times anyway
            else:
                # traverse adj list, and see if any are shorter than current dist
                for v in self.vertices[current].adj:
                    temp = distances[current] + weight(self.vertices[current],
                                                       self.vertices[v])
                    if distances[v] > temp:
                        distances[v] = temp
                        predecessors[v] = current
                        queue.enqueue((temp, v))  # shouldn't this be (distances[v], v)

        count = 0
        for distance in distances:
            if (distance != float("inf")):
                count+=1

        #print((distances[b], predecessors[b], count))

        return (distances, predecessors, count)

    def aStar(self, a, b):
        distances = [float("inf") for _ in self.vertices]
        distances[a] = 0
        predecessors = [None for _ in self.vertices]
        # queue = PriorityQueue()
        queue = PriorityQueue()
        queue.enqueue((distances[a], self.vertices[a].label))

        while True:
            if queue.empty():
                break
            # print(queue)
            _, current = queue.dequeue()
            if current is b:
                break
            # dequeue a node we already looked at
            # this may not be necessary because it will just not decrease any travel times anyway
            else:
                # traverse adj list, and see if any are shorter than current dist
                for v in self.vertices[current].adj:
                    temp = distances[current] + weight(self.vertices[current],
                                                       self.vertices[v])
                    est = temp + weight(self.vertices[v], self.vertices[b])
                    if distances[v] > temp:
                        distances[v] = temp
                        predecessors[v] = current
                        queue.enqueue((est, v))  # shouldn't this be (distances[v], v)

        count = 0
        for distance in distances:
            if (distance != float("inf")):
                count+=1

        #print((distances[b], predecessors[b], count))

        return (distances, predecessors, count)


def weight(a, b):
    return sqrt((a.longitude - b.longitude)**2 +
                (a.latitude  - b.latitude)**2)

# list of distance
# DONE

# set all to inf
# DONE

# set the source vertex distance to 0
# DONE

## create a priority queue of all the distances  call it H
# DONE

##while H is not empty
# DONE

# U=  min from H
# DONE
#remove min from H
# DONE

# check is U vertex the destination
# DONE
# if so return distance
# DONE

#else go through Adjancey list for the vertex
# DONE

#if new distance which is distance to current vertex + distance to next vertex < old distance
# DONE
# change the distance to the new shorter one
# DONE
# update piroirty queue
#if vertix not found return inf
#
