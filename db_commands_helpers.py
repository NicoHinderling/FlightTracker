def getParams(origin, destination, round_trip, departure_date, return_date=None):
    slice = [
        {
          "origin": origin,
          "destination": destination,
          "date": round_trip
        }
    ]

    if round_trip == True 
        if return_date == None:
            return "Please add your return date"
        else:
            slice.append({
                    "origin": destination,
                    "destination": origin,
                    "date": departure_date
                })
    params = {
        "request": {
            "passengers": {
                "adultCount": 1
            },
            "solutions": 2,
            "slice": slice 
            }
        }    
    return params