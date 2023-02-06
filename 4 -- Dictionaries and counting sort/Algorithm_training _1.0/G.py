import sys


def db():
    def add_user(name, database):
        if name not in database:
            database[name] = 0

    database = {}
    for seq in sys.stdin.readlines():
        command = seq.strip().split()[0]
        if command == 'DEPOSIT':
            name = seq.strip().split()[1]
            add_user(name, database)
            database[name] += int(seq.strip().split()[-1])
        elif command == 'WITHDRAW':
            name = seq.strip().split()[1]
            add_user(name, database)
            database[name] -= int(seq.strip().split()[-1])
        elif command == 'BALANCE':
            name = seq.strip().split()[1]
            if name not in database:
                print('ERROR')
            else:
                print(database[name])
        elif command == 'TRANSFER':
            name1 = seq.strip().split()[1]
            name2 = seq.strip().split()[2]
            add_user(name1, database)
            add_user(name2, database)
            summ = int(seq.strip().split()[3])
            database[name1] -= int(summ)
            database[name2] += int(summ)
        elif command == 'INCOME':
            for user in database:
                if database[user] > 0:
                    database[user] += int(database[user] * 0.01 * int(seq.strip().split()[1]))


if __name__ == '__main__':
    db()