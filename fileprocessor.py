def process_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        line_lists = [line.strip().split(':') for line in lines]
        return line_lists

if __name__ == '__main__':
    file_lists = process_file('sample.txt')
    print(file_lists)
    
