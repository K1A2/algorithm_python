def solution(fees, records):
    car_in = dict()
    car_time = dict()
    for r in records:
        time, num, m = r.split(" ")
        if m == 'IN':
            car_in[num] = time
        else:
            in_time = list(map(int, car_in.pop(num).split(":")))
            out_time = list(map(int, time.split(":")))
            time_in = (out_time[0] - in_time[0]) * 60 + out_time[1] - in_time[1]
            if num in car_time:
                car_time[num] += time_in
            else:
                car_time[num] = time_in
    for num, time_in in car_in.items():
        in_time = list(map(int, time_in.split(":")))
        out_time = [23, 59]
        time_in = (out_time[0] - in_time[0]) * 60 + out_time[1] - in_time[1]
        if num in car_time:
            car_time[num] += time_in
        else:
            car_time[num] = time_in
    times = car_time.items()
    times = sorted(times, key=lambda x:x[0])
    answer = []
    for num, time in times:
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1]
            time -= fees[0]
            fee += (time // fees[2] + (1 if time % fees[2] else 0)) * fees[3]
            answer.append(fee)
    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]) == [14600, 34400, 5000])
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]) == [0, 591])
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]) == [14841])