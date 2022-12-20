'''
To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet
marker in the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a
sequence of four characters that are all different.

How many characters need to be processed before the first start-of-packet marker is detected?
'''


raw_input = open("day_six_input.txt", "r")

processed_characters = 0
packet_marker = []

for value in raw_input.read():
    processed_characters += 1

    packet_marker.append(value)

    # part two is checking for length 14 of non-repeats.

    if len(packet_marker) > 14:
        packet_marker.pop(0)

    doubles = None

    # part two is checking for length 14 of non-repeats.

    if len(packet_marker) >= 14:
        for character in packet_marker:
            total_times = 0
            for spot in range(0, len(packet_marker)):
                if character == packet_marker[spot]:
                    total_times += 1

                if total_times > 1:
                    doubles = True
                    break

        if doubles != True:
            print(f"the first marker is at character {processed_characters}")
            break

print(packet_marker)

