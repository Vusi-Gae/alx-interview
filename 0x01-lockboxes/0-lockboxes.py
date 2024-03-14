#!/usr/bin/python3

from collection import deque

def canUnlockAll(boxes):
    num_boxes = len(boxes)  # Total number of boxes
    unlocked = [False] * num_boxes # Track if each box is unlocked
    unlocked[0] = True  # The first box is initially unlock
    queue = deque([0])  # Start BFS from the first box
    
    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)
                
    return all(unlocked)
