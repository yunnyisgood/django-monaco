from titanic.views.controller import Controller


if __name__ == '__main__':
    controller = Controller()
    while 1:
        menu = input('0-Exit 1-Preprocess')
        if menu == '0':
            break
        elif menu == '1':
            controller.preprocess('train.csv')
        else:
            continue

