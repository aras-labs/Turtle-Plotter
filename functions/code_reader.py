import numpy as np

def code_reader(filename, config):
    """Reads a code file and returns a list of points."""
    K = float(config["machine"]["width"])

    def line_to_xy(l1, l2):
        x_ = (l1**2 - l2**2)/(2*K) + K/2
        y_ = np.sqrt(l1**2 - x_**2)
        return x_, -y_
    
    with open(filename, 'r') as f:
        lines = f.readlines()

    points = []
    seq = []
    pen_state = False
    for line in lines:
        params = line.split(',')
        if params[0] == 'C14':
            pen_state = False
        elif params[0] == "C13":
            pen_state = True
        elif params[0] == "C17":
            if pen_state:
                seq.append(line_to_xy(float(params[1])/10.0, float(params[2])/10.0))
            else:
                if len(seq) > 1:
                    points.append(seq)
                seq = [line_to_xy(float(params[1])/10.0, float(params[2])/10.0)]

    return np.array(points)


if __name__ == '__main__':
    filename = "files/code.txt"
    config = {
        "controller": {
            "page": {
                "width": 710,
            }
        }
    }
    print(code_reader(filename=filename, config=config))