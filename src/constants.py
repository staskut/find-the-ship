row_borders = [60, 115, 165, 215, 270, 320, 370, 425,]
col_borders = [55, 180, 320, 455, 595,]
offset = 5
row_names = ["1", "2", "3", "4", "5", "6", "7",]
col_names = ["A", "B", "C", "D",]
rect_names = [r+c for r in row_names for c in col_names]
cells_per_image = len(row_names) * len(col_names)
headings = {"East": 0, "West": 1,}
ship_types = {"Cruiser-1": 0, "Cruiser-2": 1, "Cruiser-3": 2, "Freighter": 3, "Fishing-1": 4, "Fishing-2": 5, "Empty": 6,}
