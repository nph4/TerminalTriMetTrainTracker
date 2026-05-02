from enum import Enum


class Line(Enum):
    BLUE   = "Blue"
    RED    = "Red"
    YELLOW = "Yellow"
    GREEN  = "Green"
    ORANGE = "Orange"


class Direction(Enum):
    EASTBOUND  = "Eastbound"
    WESTBOUND  = "Westbound"
    NORTHBOUND = "Northbound"
    SOUTHBOUND = "Southbound"


# ---------------------------------------------------------------------------
# Interlined stops – defined once, referenced by multiple lines below.
# ---------------------------------------------------------------------------

# Blue + Red (west side tunnel and Beaverton corridor)
_BEAVERTON_TC          = {Direction.EASTBOUND: 9821,  Direction.WESTBOUND: 9818}
_BEAVERTON_CREEK       = {Direction.EASTBOUND: 9822,  Direction.WESTBOUND: 9819}
_BEAVERTON_CENTRAL     = {Direction.EASTBOUND: 9824,  Direction.WESTBOUND: 9823}
_MILLIKAN_WAY          = {Direction.EASTBOUND: 9826,  Direction.WESTBOUND: 9825}
_MERLO_RD              = {Direction.EASTBOUND: 9828,  Direction.WESTBOUND: 9827}
_ELMONICA              = {Direction.EASTBOUND: 9830,  Direction.WESTBOUND: 9829}
_SUNSET_TC             = {Direction.EASTBOUND: 9969,  Direction.WESTBOUND: 9624}
_WASHINGTON_PARK       = {Direction.EASTBOUND: 10120, Direction.WESTBOUND: 10121}
_GOOSE_HOLLOW          = {Direction.EASTBOUND: 10118, Direction.WESTBOUND: 10117}
_PROVIDENCE_PARK       = {Direction.EASTBOUND: 9758,  Direction.WESTBOUND: 9757}

# Blue + Red (downtown Morrison St EB / Yamhill St WB one-way couplet)
# Stops that exist on only one street of the couplet have a single direction key.
_LIBRARY_SW_9TH        = {Direction.EASTBOUND: 8333}
_PIONEER_SQUARE_SOUTH  = {Direction.EASTBOUND: 8334}
_YAMHILL_DISTRICT      = {Direction.EASTBOUND: 8336}
_GALLERIA_SW_10TH      = {Direction.WESTBOUND: 8384}
_PIONEER_SQUARE_NORTH  = {Direction.WESTBOUND: 8383}
_MORRISON_SW_3RD       = {Direction.WESTBOUND: 8381}
_OAK_SW_1ST            = {Direction.EASTBOUND: 8337,  Direction.WESTBOUND: 8380}
_OLD_TOWN_CHINATOWN    = {Direction.EASTBOUND: 8339,  Direction.WESTBOUND: 8378}

# Blue + Red + Green (Banfield corridor, Rose Quarter <-> Gateway)
_ROSE_QUARTER_TC       = {Direction.EASTBOUND: 8340,  Direction.WESTBOUND: 8377}
_CONVENTION_CENTER     = {Direction.EASTBOUND: 8341,  Direction.WESTBOUND: 8376}
_NE_7TH_AVE            = {Direction.EASTBOUND: 8342,  Direction.WESTBOUND: 8375}
_LLOYD_CENTER          = {Direction.EASTBOUND: 8343,  Direction.WESTBOUND: 8374}
_HOLLYWOOD_TC          = {Direction.EASTBOUND: 8344,  Direction.WESTBOUND: 8373}
_NE_60TH_AVE           = {Direction.EASTBOUND: 8345,  Direction.WESTBOUND: 8372}
_NE_82ND_AVE           = {Direction.EASTBOUND: 8346,  Direction.WESTBOUND: 8371}
_GATEWAY_TC            = {Direction.EASTBOUND: 8370,  Direction.WESTBOUND: 8347}

# Yellow + Green + Orange (downtown SW 6th Ave NB / SW 5th Ave SB one-way couplet)
_NW_6TH_DAVIS          = {Direction.NORTHBOUND: 9299}
_UNION_STATION_6TH     = {Direction.NORTHBOUND: 7763}
_SW_6TH_PINE           = {Direction.NORTHBOUND: 7787}
_SW_6TH_MADISON        = {Direction.NORTHBOUND: 13123}
_PIONEER_COURTHOUSE    = {Direction.NORTHBOUND: 7777}
_PSU_URBAN_CENTER_6TH  = {Direction.NORTHBOUND: 7774}
_PSU_SOUTH_6TH         = {Direction.NORTHBOUND: 10293}  # Yellow + Green + Orange
_NW_5TH_COUCH          = {Direction.SOUTHBOUND: 9303}
_UNION_STATION_5TH     = {Direction.SOUTHBOUND: 7601}
_CITY_HALL_SW_5TH      = {Direction.SOUTHBOUND: 7608}
_SW_5TH_OAK            = {Direction.SOUTHBOUND: 7627}
_PIONEER_PLACE         = {Direction.SOUTHBOUND: 7646}
_PSU_URBAN_CENTER_5TH  = {Direction.SOUTHBOUND: 7618}
_PSU_SOUTH_5TH         = {Direction.SOUTHBOUND: 7606}   # Yellow + Green + Orange


# ---------------------------------------------------------------------------
# Main stop table. Direction keys reflect the direction a train is traveling
# when it serves that platform (i.e., the direction you board to go that way).
# Terminus stations carry only the outbound direction.
# Stop IDs sourced from TriMet GTFS feed (2026-04-20).
# ---------------------------------------------------------------------------
STOPS: dict[Line, dict[str, dict[Direction, int]]] = {

    # -----------------------------------------------------------------------
    Line.BLUE: {  # Hillsboro (Hatfield Govt Center) <-> Gresham (Cleveland Ave)
    # -----------------------------------------------------------------------
        "Hatfield Government Center":    {Direction.EASTBOUND: 9848},           # western terminus
        "Hillsboro Central/SE 3rd TC":   {Direction.EASTBOUND: 9846,  Direction.WESTBOUND: 9845},
        "Hillsboro Health District":     {Direction.EASTBOUND: 9843,  Direction.WESTBOUND: 9844},
        "Washington/SE 12th Ave":        {Direction.EASTBOUND: 9841,  Direction.WESTBOUND: 9842},
        "Hillsboro Airport/Fairgrounds": {Direction.EASTBOUND: 9838,  Direction.WESTBOUND: 9837},
        "Hawthorn Farm":                 {Direction.EASTBOUND: 9839,  Direction.WESTBOUND: 9840},
        "Orenco":                        {Direction.EASTBOUND: 9835,  Direction.WESTBOUND: 9836},
        "Quatama":                       {Direction.EASTBOUND: 9834,  Direction.WESTBOUND: 9833},
        "Willow Creek/SW 185th Ave TC":  {Direction.EASTBOUND: 9831,  Direction.WESTBOUND: 9832},
        "Elmonica/SW 170th Ave":         _ELMONICA,
        "Merlo Rd/SW 158th Ave":         _MERLO_RD,
        "Millikan Way":                  _MILLIKAN_WAY,
        "Beaverton Central":             _BEAVERTON_CENTRAL,
        "Beaverton TC":                  _BEAVERTON_TC,
        "Beaverton Creek":               _BEAVERTON_CREEK,
        "Sunset TC":                     _SUNSET_TC,
        "Washington Park":               _WASHINGTON_PARK,
        "Goose Hollow/SW Jefferson St":  _GOOSE_HOLLOW,
        "Providence Park":               _PROVIDENCE_PARK,
        # Downtown Morrison St (EB) / Yamhill St (WB) couplet
        "Library/SW 9th Ave":            _LIBRARY_SW_9TH,
        "Pioneer Square South":          _PIONEER_SQUARE_SOUTH,
        "Yamhill District":              _YAMHILL_DISTRICT,
        "Galleria/SW 10th Ave":          _GALLERIA_SW_10TH,
        "Pioneer Square North":          _PIONEER_SQUARE_NORTH,
        "Morrison/SW 3rd Ave":           _MORRISON_SW_3RD,
        "Oak/SW 1st Ave":                _OAK_SW_1ST,
        "Old Town/Chinatown":            _OLD_TOWN_CHINATOWN,
        # Banfield corridor (shared with Red + Green)
        "Rose Quarter TC":               _ROSE_QUARTER_TC,
        "Convention Center":             _CONVENTION_CENTER,
        "NE 7th Ave":                    _NE_7TH_AVE,
        "Lloyd Center/NE 11th Ave":      _LLOYD_CENTER,
        "Hollywood/NE 42nd Ave TC":      _HOLLYWOOD_TC,
        "NE 60th Ave":                   _NE_60TH_AVE,
        "NE 82nd Ave":                   _NE_82ND_AVE,
        "Gateway/NE 99th Ave TC":        _GATEWAY_TC,
        # Eastern Blue Line exclusive
        "E 102nd Ave":                   {Direction.EASTBOUND: 8348,  Direction.WESTBOUND: 8369},
        "E 122nd Ave":                   {Direction.EASTBOUND: 8349,  Direction.WESTBOUND: 8368},
        "E 148th Ave":                   {Direction.EASTBOUND: 8350,  Direction.WESTBOUND: 8367},
        "E 162nd Ave":                   {Direction.EASTBOUND: 8351,  Direction.WESTBOUND: 8366},
        "E 172nd Ave":                   {Direction.EASTBOUND: 8352,  Direction.WESTBOUND: 8365},
        "E 181st Ave":                   {Direction.EASTBOUND: 8353,  Direction.WESTBOUND: 8364},
        "Rockwood/E 188th Ave":          {Direction.EASTBOUND: 8354,  Direction.WESTBOUND: 8363},
        "Ruby Junction/E 197th Ave":     {Direction.EASTBOUND: 8355,  Direction.WESTBOUND: 8362},
        "Civic Drive":                   {Direction.EASTBOUND: 13450, Direction.WESTBOUND: 13449},
        "Gresham City Hall":             {Direction.EASTBOUND: 8356,  Direction.WESTBOUND: 8361},
        "Gresham Central TC":            {Direction.EASTBOUND: 8357,  Direction.WESTBOUND: 8360},
        "Cleveland Ave":                 {Direction.WESTBOUND: 8359},                            # eastern terminus
    },

    # -----------------------------------------------------------------------
    Line.RED: {  # Beaverton TC <-> Portland Int'l Airport
    # -----------------------------------------------------------------------
        # Western terminus + shared Blue corridor
        "Beaverton TC":                  _BEAVERTON_TC,
        "Beaverton Creek":               _BEAVERTON_CREEK,
        "Elmonica/SW 170th Ave":         _ELMONICA,
        "Merlo Rd/SW 158th Ave":         _MERLO_RD,
        "Millikan Way":                  _MILLIKAN_WAY,
        "Beaverton Central":             _BEAVERTON_CENTRAL,
        "Sunset TC":                     _SUNSET_TC,
        "Washington Park":               _WASHINGTON_PARK,
        "Goose Hollow/SW Jefferson St":  _GOOSE_HOLLOW,
        "Providence Park":               _PROVIDENCE_PARK,
        # Downtown Morrison/Yamhill couplet (shared with Blue)
        "Library/SW 9th Ave":            _LIBRARY_SW_9TH,
        "Pioneer Square South":          _PIONEER_SQUARE_SOUTH,
        "Yamhill District":              _YAMHILL_DISTRICT,
        "Galleria/SW 10th Ave":          _GALLERIA_SW_10TH,
        "Pioneer Square North":          _PIONEER_SQUARE_NORTH,
        "Morrison/SW 3rd Ave":           _MORRISON_SW_3RD,
        "Oak/SW 1st Ave":                _OAK_SW_1ST,
        "Old Town/Chinatown":            _OLD_TOWN_CHINATOWN,
        # Banfield corridor (shared with Blue + Green)
        "Rose Quarter TC":               _ROSE_QUARTER_TC,
        "Convention Center":             _CONVENTION_CENTER,
        "NE 7th Ave":                    _NE_7TH_AVE,
        "Lloyd Center/NE 11th Ave":      _LLOYD_CENTER,
        "Hollywood/NE 42nd Ave TC":      _HOLLYWOOD_TC,
        "NE 60th Ave":                   _NE_60TH_AVE,
        "NE 82nd Ave":                   _NE_82ND_AVE,
        "Gateway/NE 99th Ave TC":        _GATEWAY_TC,
        # Red Line exclusive (PDX airport extension, north of Gateway)
        "Parkrose/Sumner TC":            {Direction.NORTHBOUND: 10573, Direction.SOUTHBOUND: 10572},
        "Cascades":                      {Direction.NORTHBOUND: 10575, Direction.SOUTHBOUND: 10574},
        "Mt Hood Ave":                   {Direction.NORTHBOUND: 10577, Direction.SOUTHBOUND: 10576},
        "Portland Int'l Airport":        {Direction.SOUTHBOUND: 10579},                          # northern terminus
    },

    # -----------------------------------------------------------------------
    Line.YELLOW: {  # Expo Center <-> PSU
    # -----------------------------------------------------------------------
        "Expo Center":                          {Direction.SOUTHBOUND: 11498},                  # northern terminus
        "Delta Park/Vanport":                   {Direction.NORTHBOUND: 11516, Direction.SOUTHBOUND: 11499},
        "Kenton/N Denver Ave":                  {Direction.NORTHBOUND: 11515, Direction.SOUTHBOUND: 11500},
        "N Lombard TC":                         {Direction.NORTHBOUND: 11514, Direction.SOUTHBOUND: 11501},
        "Rosa Parks":                           {Direction.NORTHBOUND: 11513, Direction.SOUTHBOUND: 11502},
        "N Killingsworth St":                   {Direction.NORTHBOUND: 11512, Direction.SOUTHBOUND: 11503},
        "N Prescott St":                        {Direction.NORTHBOUND: 11511, Direction.SOUTHBOUND: 11504},
        "Overlook Park":                        {Direction.NORTHBOUND: 11510, Direction.SOUTHBOUND: 11505},
        "Albina/Mississippi":                   {Direction.NORTHBOUND: 11509, Direction.SOUTHBOUND: 11506},
        "Interstate/Rose Quarter":              {Direction.NORTHBOUND: 11508, Direction.SOUTHBOUND: 11507},
        # Downtown SW 6th Ave (NB) / SW 5th Ave (SB) couplet (shared with Green; select stops shared with Orange)
        "NW 6th & Davis":                       _NW_6TH_DAVIS,
        "Union Station/NW 6th & Hoyt":          _UNION_STATION_6TH,
        "NW 5th & Couch":                       _NW_5TH_COUCH,
        "Union Station/NW 5th & Glisan":        _UNION_STATION_5TH,
        "SW 6th & Pine":                        _SW_6TH_PINE,
        "City Hall/SW 5th & Jefferson":         _CITY_HALL_SW_5TH,
        "SW 6th & Madison":                     _SW_6TH_MADISON,
        "SW 5th & Oak St":                      _SW_5TH_OAK,
        "Pioneer Courthouse/SW 6th Ave":        _PIONEER_COURTHOUSE,
        "Pioneer Place/SW 5th Ave":             _PIONEER_PLACE,
        "PSU Urban Center/SW 6th & Montgomery": _PSU_URBAN_CENTER_6TH,
        "PSU Urban Center/SW 5th & Mill":       _PSU_URBAN_CENTER_5TH,
        "PSU South/SW 6th & College":           _PSU_SOUTH_6TH,
        "PSU South/SW 5th & Jackson":           _PSU_SOUTH_5TH,
    },

    # -----------------------------------------------------------------------
    Line.GREEN: {  # Clackamas Town Center <-> PSU
    # -----------------------------------------------------------------------
        "Clackamas Town Center TC":             {Direction.NORTHBOUND: 13132},                  # southern terminus
        "SE Fuller Rd":                         {Direction.NORTHBOUND: 13133, Direction.SOUTHBOUND: 13130},
        "SE Flavel St":                         {Direction.NORTHBOUND: 13134, Direction.SOUTHBOUND: 13129},
        "Lents/SE Foster Rd":                   {Direction.NORTHBOUND: 13135, Direction.SOUTHBOUND: 13128},
        "SE Holgate Blvd":                      {Direction.NORTHBOUND: 13136, Direction.SOUTHBOUND: 13127},
        "SE Powell Blvd":                       {Direction.NORTHBOUND: 13137, Direction.SOUTHBOUND: 13126},
        "SE Division St":                       {Direction.NORTHBOUND: 13138, Direction.SOUTHBOUND: 13125},
        "SE Main St":                           {Direction.NORTHBOUND: 13139, Direction.SOUTHBOUND: 13124},
        # Banfield corridor (shared with Blue + Red)
        "Gateway/NE 99th Ave TC":              _GATEWAY_TC,
        "NE 82nd Ave":                          _NE_82ND_AVE,
        "NE 60th Ave":                          _NE_60TH_AVE,
        "Hollywood/NE 42nd Ave TC":             _HOLLYWOOD_TC,
        "Lloyd Center/NE 11th Ave":             _LLOYD_CENTER,
        "NE 7th Ave":                           _NE_7TH_AVE,
        "Convention Center":                    _CONVENTION_CENTER,
        "Rose Quarter TC":                      _ROSE_QUARTER_TC,
        # Downtown SW 6th/5th Ave couplet (shared with Yellow)
        "NW 6th & Davis":                       _NW_6TH_DAVIS,
        "Union Station/NW 6th & Hoyt":          _UNION_STATION_6TH,
        "NW 5th & Couch":                       _NW_5TH_COUCH,
        "Union Station/NW 5th & Glisan":        _UNION_STATION_5TH,
        "SW 6th & Pine":                        _SW_6TH_PINE,
        "City Hall/SW 5th & Jefferson":         _CITY_HALL_SW_5TH,
        "SW 6th & Madison":                     _SW_6TH_MADISON,
        "SW 5th & Oak St":                      _SW_5TH_OAK,
        "Pioneer Courthouse/SW 6th Ave":        _PIONEER_COURTHOUSE,
        "Pioneer Place/SW 5th Ave":             _PIONEER_PLACE,
        "PSU Urban Center/SW 6th & Montgomery": _PSU_URBAN_CENTER_6TH,
        "PSU Urban Center/SW 5th & Mill":       _PSU_URBAN_CENTER_5TH,
        "PSU South/SW 6th & College":           _PSU_SOUTH_6TH,
        "PSU South/SW 5th & Jackson":           _PSU_SOUTH_5TH,
    },

    # -----------------------------------------------------------------------
    Line.ORANGE: {  # SE Park Ave (Milwaukie) <-> PSU
    # -----------------------------------------------------------------------
        "SE Park Ave":                          {Direction.NORTHBOUND: 13720},                  # southern terminus
        "Milwaukie/Main St":                    {Direction.NORTHBOUND: 13721, Direction.SOUTHBOUND: 13718},
        "SE Tacoma/Johnson Creek":              {Direction.NORTHBOUND: 13722, Direction.SOUTHBOUND: 13717},
        "SE Bybee Blvd":                        {Direction.NORTHBOUND: 13723, Direction.SOUTHBOUND: 13716},
        "SE 17th Ave & Holgate Blvd":           {Direction.NORTHBOUND: 13724, Direction.SOUTHBOUND: 13715},
        "SE 17th Ave & Rhine St":               {Direction.NORTHBOUND: 13725, Direction.SOUTHBOUND: 13714},
        "Clinton St/SE 12th Ave":               {Direction.NORTHBOUND: 13726, Direction.SOUTHBOUND: 13713},
        "OMSI/SE Water":                        {Direction.NORTHBOUND: 13727, Direction.SOUTHBOUND: 13712},
        "South Waterfront/S Moody":             {Direction.NORTHBOUND: 13728, Direction.SOUTHBOUND: 13711},
        "Lincoln St/SW 3rd Ave":                {Direction.NORTHBOUND: 13729, Direction.SOUTHBOUND: 13710},
        # Downtown SW 5th Ave (SB) only -- Orange skips most NB 6th Ave stops
        "NW 5th & Couch":                       _NW_5TH_COUCH,
        "Union Station/NW 5th & Glisan":        _UNION_STATION_5TH,
        "City Hall/SW 5th & Jefferson":         _CITY_HALL_SW_5TH,
        "SW 5th & Oak St":                      _SW_5TH_OAK,
        "Pioneer Place/SW 5th Ave":             _PIONEER_PLACE,
        "PSU Urban Center/SW 5th & Mill":       _PSU_URBAN_CENTER_5TH,
        "PSU South/SW 5th & Jackson":           _PSU_SOUTH_5TH,
        "PSU South/SW 6th & College":           _PSU_SOUTH_6TH,
    },
}
