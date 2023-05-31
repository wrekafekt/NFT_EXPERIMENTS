def split_file(input_file, output_folder):
    with open(input_file, 'r') as file:
        quotes = file.read().split('\n\n')

    for i, quote in enumerate(quotes):
        output_file_path = f'{output_folder}/quote_{i+1}.txt'
        with open(output_file_path, 'w') as output_file:
            output_file.write(quote)

split_file('SOURCE TEXT PATH', 'OUTPUT PATH')
