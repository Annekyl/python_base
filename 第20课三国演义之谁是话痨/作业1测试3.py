import openpyxl

# Create a new workbook and select the active worksheet
book = openpyxl.Workbook()
ws = book.active

# Define the range of cells to merge
merge_range = (1, 1, 3, 3)

# Merge the cells
ws[merge_range].value = "New merged value"

# Save the workbook
book.save("merged_cells.xlsx")
