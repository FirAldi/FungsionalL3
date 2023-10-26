def konversi(minggu=0):
    def step1(hari=0):
        def step2(jam=0):
            def step3(menit=0):
                total_menit = ((minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit)
                return total_menit
            return step3
        return step2
    return step1

data = [
    "2 minggu 6 hari 3 jam 17 menit",
    "3 minggu 11 hari 7 jam 18 menit",
    "6 minggu 2 hari 6 jam 25 menit"
]

outputData = []

for item in data:
    parts = item.split()
    minggu = int(parts[0])
    hari = int(parts[2])
    jam = int(parts[4])
    menit = int(parts[6])
    konvert = konversi(minggu)(hari)(jam)(menit)
    outputData.append(konvert)

print("Output Data =", outputData)