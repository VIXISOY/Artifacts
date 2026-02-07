import json

class WrongLayerException(Exception):
    pass

class InexistentPositionException(Exception):
    pass

"open the POI.json file and load it"
with open('POI.json') as POIjson:
    POI = json.load(POIjson)
    print(POIjson)


def poi(poi, layer, Debug = 0):
    """
    give the x,y location of a point of interest
    
    :param poi: name of the point of interest
    :param layer: current layer of the character
    :param Debug: debug tag

    :return: x,y coordinates of the point of interest
    :raises:
        :WrongLayerException: if the character is in the wrong layer
    :raises:
        :InexistentPositionException: if the point of interest does not exist
    """
    if poi in POI:
        if layer not in POI[poi]["layer"]:
            raise WrongLayerException(f"player in wrong layer: {layer}")
        return POI[poi]["x"], POI[poi]["y"]
    raise InexistentPositionException(f"POI {poi} not found")

if __name__ == "__main__":
    print(POI["chicken"])
    print(poi("chicken", "Overworld"))
    
    try:
        print(poi("chicken", "Underworld"))
    except WrongLayerException as e:
        print(e)

    try:
        print(poi("chicken2", "Overworld"))
    except InexistentPositionException as e:
        print(e)
