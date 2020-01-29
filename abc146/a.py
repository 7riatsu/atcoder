def search(s):
    week_day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    for i in range(len(week_day)):
        if s == week_day[i]:
            return len(week_day) - i

if __name__ == "__main__":
    s = input()
    print(search(s))