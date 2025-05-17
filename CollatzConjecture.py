def collatz_conjecture(number):
    total_steps = 0
    sequence = [number]
    while True:
        if(number%2==0):
            number = int(number/2)
        else:
            number = int((3*number)+1)
        
        total_steps += 1
        sequence.append(number)
        
        if number==1:
            break
    return total_steps, sequence

collatz_conjecture()
