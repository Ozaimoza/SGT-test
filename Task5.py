def cheerleader(lines, cheers):
    for i in range(lines):
        print(' ' * (i * 3) + 'Go' + ' Team Go' * (cheers - 1))

# Contoh penggunaan
cheerleader(2, 1)