stations = {}


# Total number of areas
tot_area = 12

def fill_stations(stations):
    stations['A'] = set([0,1,2])
    stations['B'] = set([1,2,3,4])
    stations['C'] = set([1,5,6])
    stations['D'] = set([0, 1,2,3,4,7])
    stations['E'] = set([3,8,9,10])
    stations['F'] = set([1,3,4,7,8,9])

# This is a O(n^2) greedy algo
def find_stations(stations):
    # Covered areas
    covered = set()
    # Selected stations
    sel_sta = set()

    while True:
        if len(covered) == tot_area:
            return (covered, sel_sta)
        
        # Set that adds the most coverage
        max_set = ""
        # The number of stations that set adds
        max_cov = 0

        # Find the set that adds the most coverage to the covered areas
        for (sta, sta_set) in stations.items():
            diff = len(sta_set - covered)
            
            if diff > max_cov:
                max_cov = diff
                max_set = sta
                
        if max_cov == 0:
            return (covered, sel_sta)

        # Add the station
        covered.update(stations[max_set])
        sel_sta.add(max_set)

if __name__ == "__main__":
    fill_stations(stations)

    (covered, sel_sta) = find_stations(stations)

    if len(covered) == 0:
        print("There are no stations")
    elif len(covered) == tot_area:
        print("Stations {} cover all areas".format(sel_sta))
    else:
        print("Stations {} cover areas {}".format(sel_sta, covered))
