class Servo(object):
    def __init__(self, channel, comm):
        if not comm.is_open:
            raise ValueError("comm port is not open")
        self.channel = channel
        self.comm = comm

        self.write(-1.0)

    def write(self, position):
    	if position < -1.0 or position > 1.0:
    		raise ValueError("{} not in range (-1.0, 1.0)".format(position))

        self.comm.write(
            "#{}P{}\r".format(
                self.channel,
                str(int(500*(position+1) + 1000))
            ).encode('utf-8')
        )

        self.position = position
