emptySign=' 0 '
assignedSign=' ■ '
attacked=' X '
checkList=[]
lastCoordinates=[None,None]

class Board:

    def __init__(self):
        self.X = 6
        self.Y = 6
        self.bo = [[emptySign for i in range(self.X)] for y in range(self.Y)]

    def empty_board(self):
        self.bo = [[emptySign for i in range(self.X)] for y in range(self.Y)]

    def create_new_board(self):
        print('=============================================')
        print(f' W E L C O M E  T O  S E A B A T T L E ! ! ! ')
        print('=============================================\r\n')
        print('   y\X|  1  |  2  |  3  |  4  |  5  |  6  | ',end='')
        for i in range(self.X):
            print(f'         ', end='\r\n')
            print(f'   {i+1}  | ',end='')
            for y in range(self.Y):
                print(self.bo[i][y],end=' | ')
        print('')
        print(f'=============================================\r\n')
        create_new_board=self.bo
        return self.bo



    def print_board(self,bo):
        print('=============================================')
        print(f' W E L C O M E  T O  S E A B A T T L E ! ! ! ')
        print('=============================================\r\n')
        print('   y\X|  1  |  2  |  3  |  4  |  5  |  6  | ',end='')
        for i in range(self.X):
            print(f'         ', end='\r\n')
            print(f'   {i+1}  | ',end='')
            for y in range(self.Y):
                print(self.bo[i][y],end=' | ')
        print('')
        print(f'=============================================\r\n')
        return bo


class Ship:

    def __init__(self,b):
        self.current_state=b.bo
        chX=0
        chY=0

    def board_reinitialization(self,b):
        b.empty_board()
        self.current_state = b.bo
        chX = 0
        chY = 0

    def is_cell_empty(self,chY,chX):
            if self.current_state[chY][chX] == emptySign:
                return True
            else:
               return False
    def is_cells_between_one_and_six(self,chY,chX):
            if 6>=chX>0 and 6>=chY>0:
                return True
            else:
                return False
    def surround_cells_check(self,checkList,chY,chX,lastCoordinates,number_of_points,nu_of_po):
        for val in checkList:
            print(f'chY:{chY}:chX:{chX}:last{lastCoordinates[0]}:val0:{val[0]}:val1:{val[1]}:{lastCoordinates[0]==val}')
            if (nu_of_po==0):
                if (self.current_state[val[0]][val[1]] != emptySign ):
                    b.print_board(self.current_state)
                    print('Корабли должны находится на расстоянии минимум одна клетка друг от друга. Введите новые координы! ')
                    return False
            elif(nu_of_po==1):
                if (self.current_state[val[0]][val[1]] != emptySign):
                    if  lastCoordinates[0] != val:
                        b.print_board(self.current_state)
                        print('Корабли должны находится на расстоянии минимум одна клетка друг от друга. Введите новые координы!')
                        return False
            elif(nu_of_po==2):
                if (self.current_state[val[0]][val[1]] != emptySign):
                    if lastCoordinates[0] != val:
                        b.print_board(self.current_state)
                        print('Корабли должны находится на расстоянии минимум одна клетка друг от друга.Введите новые координы!')
                        return False

        return True




    def is_that_cell_is_allowed_to_allocate(self,chY,chX,number_of_points,nu_of_po):


           if 0<chY<5:

                if 0<chX<5:

                    checkList.clear()
                    checkList.append([chY - 1,chX])       #1
                    checkList.append([chY - 1, chX + 1])  #2
                    checkList.append([chY,chX + 1])       #3
                    checkList.append([chY + 1, chX + 1])  #4
                    checkList.append([chY + 1, chX])      #5
                    checkList.append([chY + 1, chX - 1])  #6
                    checkList.append([chY, chX - 1])      #7
                    checkList.append([chY - 1, chX - 1])  #8
                    return self.surround_cells_check(checkList,chY,chX,lastCoordinates,number_of_points,nu_of_po)

                elif chX==5:
                    checkList.clear()
                    checkList.append([chY - 1, chX])      # 1
                    checkList.append([chY + 1, chX])      # 5
                    checkList.append([chY + 1, chX - 1])  # 6
                    checkList.append([chY, chX - 1])      # 7
                    checkList.append([chY - 1, chX - 1])  # 8
                    return self.surround_cells_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po)

                elif chX==0:

                    checkList.clear()
                    checkList.append([chY - 1, chX])      # 1
                    checkList.append([chY - 1, chX + 1])  # 2
                    checkList.append([chY, chX + 1])      # 3
                    checkList.append([chY + 1, chX + 1])  # 4
                    checkList.append([chY + 1, chX])      # 5

                    return self.surround_cells_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po)

           elif chY==5:

               if 0 < chX < 5:
                    checkList.clear()
                    checkList.append([chY - 1, chX])      # 1
                    checkList.append([chY - 1, chX + 1])  # 2
                    checkList.append([chY, chX + 1])      # 3
                    checkList.append([chY, chX - 1])      # 7
                    checkList.append([chY - 1, chX - 1])  # 8
                    return self.surround_cells_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po)
               elif chX == 5:
                    checkList.clear()
                    checkList.append([chY - 1, chX])      # 1
                    checkList.append([chY, chX - 1])      # 7
                    checkList.append([chY - 1, chX - 1])  # 8
                    return self.surround_cells_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po)
               elif chX == 0:
                    checkList.clear()
                    checkList.append([chY - 1, chX])  # 1
                    checkList.append([chY - 1, chX + 1])  # 2
                    checkList.append([chY, chX + 1])  # 3
                    return self.surround_cells_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po)

           elif chY==0:

               if 0 < chX < 5:
                    checkList.clear()
                    checkList.append([chY, chX + 1])      # 3
                    checkList.append([chY + 1, chX + 1])  # 4
                    checkList.append([chY + 1, chX])      # 5
                    checkList.append([chY + 1, chX - 1])  # 6
                    checkList.append([chY, chX - 1])      # 7
                    return self.surround_cells_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po)
               elif chX == 5:
                    checkList.clear()
                    checkList.append([chY + 1, chX])      # 5
                    checkList.append([chY + 1, chX - 1])  # 6
                    checkList.append([chY, chX - 1])      # 7
                    return self.surround_cells_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po)
               elif chX == 0:
                    checkList.clear()
                    checkList.append([chY, chX + 1])      # 3
                    checkList.append([chY + 1, chX + 1])  # 4
                    checkList.append([chY + 1, chX])      # 5
                    return self.surround_cells_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po)





    def check_coordinates(self,number_of_points,number_of_ships,type_of_player):
        nu_of_po=0
        nu_of_sh=0

        try:
            while nu_of_sh < number_of_ships:
                while nu_of_po <number_of_points:

                    chX = int(input(f'Пожалуйста введите координату {nu_of_po+1} корабля №{nu_of_sh+1} (3 клетки) X=: '))
                    chY = int(input(f'Пожалуйста введите координаты {nu_of_po+1} корабля №{nu_of_sh+1} (3 клетки) Y=: '))
                    if self.is_cells_between_one_and_six(chY,chX):
                        chX -= 1
                        chY -= 1

                        if self.is_cell_empty(chY,chX):

                            if self.is_that_cell_is_allowed_to_allocate(chY,chX,number_of_points, nu_of_po):
                                lastCoordinates.clear()
                                lastCoordinates.append([chY,chX])
                                self.current_state[chY][chX]=' ■ '
                                b.print_board(self.current_state)
                            else:
                                nu_of_po -= 1

                        else:
                            b.print_board(self.current_state)
                            print(f'Данная координата уже занята!')
                            nu_of_po -= 1
                    else:
                       b.print_board(self.current_state)
                       print(f'Неправильно введены координаты. Пожалуйста введите числа от 1 до 6!')
                       nu_of_po-=1

                    nu_of_po += 1
                nu_of_sh+=1
                nu_of_po=0

        except ValueError:
            self.board_reinitialization(b)
            b.print_board(self.current_state)
            print('Пожалуйста вводите заново все координаты. Разрешены только цифры от 1 до 6!')
            return self.check_coordinates(number_of_points,number_of_ships,type_of_player)



    def initiate_user_ships(self):
        self.check_coordinates(3,2,'user')
        #check_coordinates(self, 2, 2, 'user')
        #check_coordinates(self, 1, 4, 'user')




b=Board()
b.create_new_board()

c=Ship(b)
c.initiate_user_ships()











