time = int(input())
hours = time // 3600
time2 = time - hours * 3600
mins = time2 // 60
secs = time % 60
print(f"{hours:02d}:{mins:02d}:{secs:02d}")