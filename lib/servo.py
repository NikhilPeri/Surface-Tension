class Servo(object):
    def __init__(self, channel, com):
        if not com.is_open:
            raise ValueError("COM port is not open")
        self.channel = channel
        self.com = com

        self.write(-1.0)

    def write(self, position):
    	if position < -1.0 or position > 1.0:
    		raise ValueError("{} not in range (-1.0, 1.0)".format(position))

        self.com.write(
            "#{}P{}\r".format(
                self.channel,
                str(int(500*(position+1) + 1000))
            ).encode('utf-8')
        )

        self.position = position
