def gradient(text):
    lines = text.split('\n')
    total = len(lines)
    
    for i, line in enumerate(lines):
        if i < total // 2:
            color = 34 + (i * 2)
        else:
            color = 96 + ((i - total // 2) * (1 // (total // 2)))
    
        print(f"\033[{color}m{line}\033[0m")