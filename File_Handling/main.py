# def reda_to_file (filename):
with open('myfile2', 'r') as f:
        
    size_to_read = 10
    f_contents = f.read()
        
    while len(f_contents) > 0:
        print(f_contents, end='_*_')
        f_contents = f.read(size_to_read)
            
        
        
    
# reda_to_file("myfile2.txt")