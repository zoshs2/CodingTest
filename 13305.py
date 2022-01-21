import sys

def half_calculation(segment):
    wage_list = []
    num_link = len(segment[0])
    first_city = segment[1][0]
    
    for i in range(num_link):
        front_flag = False
        later_flag = False

        front_links = segment[0][:num_link-i]
        front_wage = first_city * sum(front_links)
        if len(front_links) == num_link:
            wage_list.append(front_wage)
            continue

        elif len(front_links) > 1:
            front_cities = segment[1][:-i]
            front_segment = [front_links, front_cities]
            front_wlist = half_calculation(front_segment)
            front_flag = True

        later_links = list(reversed(list(reversed(segment[0]))[:i]))
        later_cities = list(reversed(list(reversed(segment[1]))[:i+1]))
        if len(later_links) > 1:
            later_segment = [later_links, later_cities]
            later_wlist = half_calculation(later_segment)
            later_flag = True

        later_wage = later_cities[0] * sum(later_links)
        if front_flag is True and later_flag is False:
            for j, fw in enumerate(front_wlist):
                front_wlist[j] = fw + later_wage
            wage_list.extend(front_wlist)
            continue

        elif front_flag is False and later_flag is True:
            for j, lw in enumerate(later_wlist):
                later_wlist[j] = lw + front_wage
            wage_list.extend(later_wlist)
            continue

        elif front_flag is True and later_flag is True:
            all_wlist = []
            for fw in front_wlist:
                for lw in later_wlist:
                    all_wlist.append(fw + lw)
            wage_list.extend(all_wlist)
            continue
        
        wage_list.append(front_wage + later_wage)
    
    return wage_list

def main():
    data = []
    for _ in range(3):
        line_data = list(map(int, sys.stdin.readline().split()))
        data.append(line_data)

    wage = half_calculation(data[1:])
    print(wage)

if __name__ == '__main__':
    main()