def sort_by_shablon(len_main, len_shablon, main, shablon):
    main_to_shablon = []
    i = 0
    while i < len_shablon:
        if shablon[i] in main:
            main_to_shablon.append(shablon[i])
            main.remove(shablon[i])
        else:
            i += 1

    if len(main) != 0:
        main = sorted(main)
        main_to_shablon = main_to_shablon + main

    return main_to_shablon


if __name__ == '__main__':
    m = int(input())
    mas_m = (list(map(int, input().split())))
    n = int(input())
    mas_n = (list(map(int, input().split())))
    sort_mass = sort_by_shablon(m, n, mas_m, mas_n)
    print(" ".join(map(str, sort_mass)))
