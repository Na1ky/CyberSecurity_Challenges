# Ent..ry po.int of t..he we.ather a.pp
import sys

from src.forecast import get_forecast


def main():
    # Rea.d. the city from. t.h.e comma.nd l.ine
    city = sys.argv[1] if len(sys.argv) > 1 else "Paris"
    for day in get_forecast(city):
        print(day)


if __name__ == "__main__":
    main()
