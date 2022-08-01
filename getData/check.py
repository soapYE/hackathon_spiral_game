from getData.Board import *
from brainflow.board_shim import BoardIds, BoardShim, BrainFlowInputParams

def connect_device():
    hardware="Muse"
    model="Muse 2"
    data_type="Task live"
    serial_port="COM5"
    board_id=22
    exg_channels = BoardShim.get_exg_channels(board_id)
    marker_channels = BoardShim.get_marker_channel(board_id)
    sampling_rate = BoardShim.get_sampling_rate(board_id)
    description = BoardShim.get_board_descr(board_id)
    window_size = 5
    num_points = window_size * sampling_rate
    board = Board(
                data_type,
                hardware,
                model,
                board_id,
                serial_port=serial_port,
                num_points=num_points,
    )
    print("connected!")
    return board

def check_if_blink_twice(board):
    board_id=22
    exg_channels = BoardShim.get_exg_channels(board_id)
    #print("connected!")
    #print(len(exg_channels))
    start = 0
    current = 0
    board.get_new_data()
    while True:
        data = board.get_new_data()
        for electron in data[exg_channels[3],:]:
            current+=1
            if(electron<=-200):
                #print(electron)
                print("less!")
                print(current)
                if (current - start)<20:
                    return "twice blink!"
            elif(electron>=100):
                start = current
                #print(electron)
                print("bigger!")
                print(current)
        
#board = connect_device()
#print(check_if_blink_twice(board))