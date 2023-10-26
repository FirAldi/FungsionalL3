data = [
    "2 minggu 6 hari 3 jam 17 menit",
    "3 minggu 11 hari 7 jam 18 menit",
    "6 minggu 2 hari 6 jam 25 menit"
]

filtered_data = []

for item in data:
    parts = item.split()
    integers = list(filter(lambda x: x.isdigit(), parts))
    filtered_data.append(integers)

print("Output Data =", filtered_data)