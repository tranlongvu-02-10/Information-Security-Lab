print("Nhap cac dong van ban (Nhap 'done' de ket thuc):")
lines = []  
while True:
    line = input()  
    if line.lower() == 'done':  
        break
    lines.append(line) 
print("\nCac dong van ban ban da nhap la:")
for line in lines:
    print(line.upper())
