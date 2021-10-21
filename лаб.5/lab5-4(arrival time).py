def time(h_dep, m_dep, h_way, m_way):
    days = 0
    hours = h_dep + h_way
    minutes = m_dep + m_way
    if minutes == 60:
        hours += 1
        m_dep = 0
    elif minutes > 60:
        hours += 1
        m_dep = m_way - (60 - m_dep)
    elif minutes < 60:
        m_dep = minutes
    if hours == 24:
        h_dep = 0
        days = 1
    elif hours > 24:
        h_dep = hours - ((hours // 24) * 24)
        days = hours // 24
    elif hours < 24:
        h_dep = hours
        days = 0
    print("{:2d}".format(h_dep), "hours", ":", "{:2d}".format(m_dep), "minutes")
    print(days)


time(int(input("Часы отправления поезда")),
     int(input("Минуты отправления поезда")),
     int(input("Часы продолжительности поездки")),
     int(input("Минуты продолжительности поездки")))
