#TWO.PY
import Package_One

Package_One.func()

print('TOP LEVEL IN TWO.PY')

if __name__ == '__main__':
    print('TWO.PY is being run directly!')
else:
    print('TWO.PY is being imported!')
