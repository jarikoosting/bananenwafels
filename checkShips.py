#!/opt/local/bin/python3.4
# Jarik Oosting
# Check if a ship got a hit


def checkShips(destroyDict):
    """
    Check if a ship has been hit
    After placement, if the user clicks, it goes to this function!
    """
    coords = {"Aircraft Carrier":[(9,2),(9,3),(9,4),(9,5)], "Battleship":[(1,1),(2,2)]}
    click = (9,3)

    # Loop through dictionary with ships and coords
    for ship, coord in coords.items():
        for el in coord:
            if click == el:
                coord.remove(el)

                shipHit = True

                # Check if ship is destroyed after the hit
                checkDestroyed()

            else:
                shipHit = False

def checkDestroyed():
    """
    Check if a ship is destroyed
    """

    # Return True when ship is destroyed

    print("Hoi")


if __name__ == "__main__":
    destroyDict = {}
    checkShips(destroyDict)
