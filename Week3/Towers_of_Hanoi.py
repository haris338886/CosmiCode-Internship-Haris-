def towers_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    towers_of_hanoi(n - 1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    towers_of_hanoi(n - 1, helper, source, destination)

towers_of_hanoi(3, 'A', 'B', 'C')



