motions = ['no_move', 'circle', 'z', 'w', 'flick']
def score(input):
    if input[5] <= 1688.0:
        if input[14] <= 686.2718505859375:
            if input[2] <= -1260.0:
                if input[0] <= -2018.0:
                    var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                else:
                    var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
            else:
                var0 = [1.0, 0.0, 0.0, 0.0, 0.0]
        else:
            var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
    else:
        var0 = [0.0, 0.0, 0.0, 0.0, 1.0]
    return var0
