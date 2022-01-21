import sys

def half_calculation(segment):
    num_link = len(segment[0])
    first_city = segment[1][0]
    
    for i in range(num_link):
        front_links = segment[0][:num_link-i]
        front_wage = first_city * sum(front_links)
        if len(front_links) == num_link:
            answer = front_wage
            continue

        elif len(front_links) > 1:
            front_cities = segment[1][:-i]
            front_segment = [front_links, front_cities]
            front_wage = half_calculation(front_segment)

        later_links = list(reversed(list(reversed(segment[0]))[:i]))
        later_cities = list(reversed(list(reversed(segment[1]))[:i+1]))
        
        if len(later_links) > 1:
            later_segment = [later_links, later_cities]
            later_wage = half_calculation(later_segment)
        else:
            later_wage = later_cities[0] * sum(later_links)
    
        if answer > front_wage + later_wage:
            answer = front_wage + later_wage
    
    return answer

def main():
    data = []
    for _ in range(3):
        line_data = list(map(int, sys.stdin.readline().split()))
        data.append(line_data)

    wage = half_calculation(data[1:])
    print(wage)

if __name__ == '__main__':
    main()