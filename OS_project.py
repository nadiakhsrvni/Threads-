from threading import Thread
from time import sleep

tailor = [0, 0, 0, 0, 0, 0, 0, 0, 0]
costumer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#each index of these two arrays will be a thread

def task_secretary(lines):
    cpt = num_of_costumers / num_of_tailors #number of costumers per tailor
    k = 0
    head_tailor = False

    for i in range(num_of_tailors):
        temp_cpt = cpt
        orders = [[]]

        while(temp_cpt>0):
            current_order = lines[k].split(' ')
            if(orders == [[]]):
                orders = [current_order]
            else:
                orders.append(current_order)
            k += 1
            temp_cpt -= 1

        if(head_tailor == False):
            boolean_haji_firooz = True
            haji_firooz = Thread(target=task_haji_firooz, args=(orders,))
            haji_firooz.start()

        else:
            tailor[i-1] = Thread(target=task_tailor, args=(orders,i-1))
            tailor[i-1].start()

    print('Secretary completes his task')


def task_haji_firooz(orders):
    print("Head tailor gets orders.")

    for i in range(len(orders)):
        for j in range(1, len(orders[i])):
            if (orders[i][j] == "shalvar"): sleep(0.7)
            if (orders[i][j] == "pirahan"): sleep(0.85)
            if (orders[i][j] == "kot"): sleep(0.9)

        print(f'Head tailor prepares order of {orders[i][0]}')

        index = find_index(orders[i][0])
        costumer[index] = Thread(target=task_costumer, args=(orders[i],))
        costumer[index].start()


def task_tailor(orders, n):
    print(f'Tailor {n+1} gets orders.')

    for i in range(len(orders)):
        for j in range(1, len(orders[i])):
            if (orders[i][j] == "shalvar"): sleep(0.8)
            if (orders[i][j] == "pirahan"): sleep(0.9)
            if (orders[i][j] == "kot"): sleep(1)

        print(f'Tailor {n+1} prepares order of {orders[i][0]}')
        print(f'Tailor {n + 1} completes his task')

        index = find_index(orders[i][0])
        costumer[index] = Thread(target=task_costumer, args=(orders[i],))
        costumer[index].start()


def task_costumer(orders):
    sum = 0
    for i in range(1, len(orders)):
        if (orders[i] == "shalvar"):
            sleep(0.4)
            sum += 23000
        if (orders[i] == "pirahan"):
            sleep(0.4)
            sum += 17000
        if (orders[i] == "kot"):
            sleep(0.5)
            sum += 30000

    print(f'{orders[0]} puts {sum} in dressing room and exits')


def find_index(costumer_name):
    for i in range(len(lines)):
        temp_array = lines[i].split(' ')
        if(temp_array[0] == costumer_name): return i


if __name__ == "__main__":
    num_of_tailors = int(input("enter number of tailors:"))
    num_of_tailors += 1  # adding Head tailor to the number of tailors
    file = open("./test.txt", "r")
    num_of_costumers = int(file.readline())

    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n')

    secretary = Thread(target=task_secretary, args=(lines,))
    secretary.start()

