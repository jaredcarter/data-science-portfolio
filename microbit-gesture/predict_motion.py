from microbit import accelerometer
from micropython import const
import array, time
from math import sqrt
import model

_num_samples = const(100)
_delay = const(5)
_threshold = const(100000)
# names of motions
motions = model.motions
def result(v):
    # get result from model
    res = model.score(v)
    # find index of most likely motion
    i = res.index(max(res))
    # return name and confidence of motion
    return (motions[i], res[i])

# columns of data we are measuring
cols = [a+'_'+b for a in ['min', 'max', 'peaks', 'mean', 'std'] for b in ['x', 'y', 'z']]
while True:
    response = input('Press Enter to measure and guess: ')
    if not response:
        # cols are x, y, z
        # rows are min, max, peaks, sum, sum2, prev, prev2
        a_ints = array.array('i', [0] * 3 * 8)
        for i in range(3):
            a_ints[i] = 2000 # initial min is very high
            a_ints[i+3] = -2000 # initial max is very low
        # cols are x, y, z
        # rows are mean and std
        a_floats = array.array('f', [0.0] * 3 * 2)
        # get measurements from accelerometer
        for j in range(_num_samples):
            curr = accelerometer.get_values()
            for i,a in enumerate(curr):
                # minimum
                if a < a_ints[i]:
                    a_ints[i] = a
                # maximum
                elif a > a_ints[i+3]:
                    a_ints[i+3] = a
                # sum
                a_ints[i+3*3] += a
                # sum of squares
                a_ints[i+3*4] += a**2
                # peak
                if (a_ints[i+3*6] - a_ints[i+3*7] > _threshold) and (a_ints[i+3*6] - a**2 > _threshold):
                    a_ints[i+3*2] += 1
                # update previous 2 points
                a_ints[i+3*7] = a_ints[i+3*6]
                a_ints[i+3*6] = a**2
                # delay
                time.sleep_ms(_delay)
        # calculate mean and std
        for i in range(3):
            a_floats[i] = a_ints[i+3*3] / _num_samples
            a_floats[i+3] = sqrt((a_ints[i+3*4] / _num_samples) - a_floats[i]**2)
        data = list(a_ints[:9]) + list(a_floats)
        # ask the model to interpret the data
        print(result(data))
