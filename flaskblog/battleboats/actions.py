from random import seed, randint


seed(1)



class LessThan(object):  # --> Change to 'LessThan'
    """
    Compares the values of two fields.

    :param fieldname:
        The name of the other field to compare to.
    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated with `%(other_label)s` and `%(other_name)s` to provide a
        more helpful error.
    """
    def __init__(self, fieldname, message=None):
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(field.gettext("Invalid field name '%s'.") % self.fieldname)
        if field.data >= other.data:  #  --> Change to >= from !=
            d = {
                'other_label': hasattr(other, 'label') and other.label.text or self.fieldname,
                'other_name': self.fieldname
            }
            message = self.message
            if message is None:
                message = field.gettext('Field must be equal to %(other_name)s.')

            raise ValidationError(message % d)

def setNumberBoats(rows, cols):
    if rows == 3 or cols == 3:
        return 1
    elif (rows > 3 and rows <= 5) or (cols > 3 and cols <= 5):
        return 2
    elif (rows > 5 and rows <= 7) or (cols > 5 and cols <= 7):
        return 3
    elif (rows > 7 and rows <= 9) or (cols > 7 and cols <= 9):
        return 4
    else:
        return 6

def setUpBoardSkeleton(rows, cols, items):
    letter_dict = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 11:"L", 12:"M"}
    letter_columns = []
    for i in range(cols):
        letter_columns.append(letter_dict.get(i))
    for i in range(rows):
        #lst = []
        for j in range(cols):
            temp_str = letter_dict.get(j) + str(i)
            items.append(temp_str)
            #lst.append(temp_str)
        #items.append(lst)
    return items, letter_columns

def randomNumberGenerator(maxLength):
    value = randint(0, maxLength-1)
    return value

def randomDirection():
    value = randint(0, 1)
    if value:
        return "DOWN"
    return "RIGHT"

def checkBoatPlacement(rowValue, colValue, direction, ship_coordinates, rows, cols):
    if (rowValue >= rows-2) and (direction == "DOWN"):
        return False
    elif (colValue >= cols-2) and (direction == "RIGHT"):
        return False
    coord_1 = [(rowValue, colValue)]
    coord_2 = []
    coord_3 = []
    if direction == "DOWN":
        temp_2 = (rowValue+1, colValue)
        temp_3 = (rowValue+2, colValue)
        coord_2.append[temp_2]
        coord_3.append[temp_3]
    else:
        temp_2 = (rowValue, colValue+1)
        temp_3 = (rowValue, colValue+2)
        coord_2.append[temp_2]
        coord_3.append[temp_3]
    if coord_1 in ship_coordinates or coord_2 in ship_coordinates or coord_3 in ship_coordinates:
        return False
    ship_coordinates.append(coord_1)
    ship_coordinates,append(coord_2)
    ship_coordinates,append(coord_3)
    return True

def randomizeBoard(rows, cols, cell_pieces, rocks, boatNumber):
    boats_placed = 0
    ship_coordinates = []
    while boats_placed < boatNumber:
        rowValue = randomNumberGenerator(rows)
        colValue = randomNumberGenerator(cols)
        direction = randomDirection()
        if checBoatkPlacement(rowValue, colValue, direction, ship_coordinates, rows, cols):
            placeBoat(cell_pieces, ship_coordinates, rowValue, colValue, direction)
            boats_placed += 1
    rocks_placed = 0
    rock_coordinates = []
    while rocks_placed < rocks:
        rowValue = randomNumberGenerator(rows)
        colValue = randomNumberGenerator(cols)
        if checkRockPlacement(rowValue, colValue, rock_coordinates, ship_coordinates, rows, cols):
            placeRock(cell_pieces, rock_coordinates, rowValue, colValue)
            total_rocks += 1
    return cell_pieces
