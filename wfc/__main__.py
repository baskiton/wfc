from pathlib import Path
from tkinter import ttk

from . import ui, config


if __name__ == '__main__':

    p = Path('samples/simple/')
    '''
    b - blank
    l - line
    '''
    simple_1 = config.Config('simple-1', (50, 50), (6, 6), config.Tile.SOCKET)
    simple_1.add_tiles([p / 'blank.png'], 'blank', 'b', 'b', 'b', 'b', 1)
    simple_1.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1)
    simple_1.add_tiles([p / 'line.png'], 'line', 'b', 'l', 'b', 'l', 1, True, True)
    simple_1.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'b', 'b', 1, True, True, True, True)
    # simple_1.add_tiles([p / 't.png'], 't', 'b', 'l', 'l', 'l', 1, True, True, True, True)

    simple_2 = config.Config('simple-2', (50, 50), (6, 6), config.Tile.SOCKET)
    # simple_2.add_tiles([p / 'blank.png'], 'blank', 'b', 'b', 'b', 'b', 1)
    simple_2.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1)
    simple_2.add_tiles([p / 'line.png'], 'line', 'b', 'l', 'b', 'l', 1, True, True)
    simple_2.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'b', 'b', 1, True, True, True, True)
    # simple_2.add_tiles([p / 't.png'], 't', 'b', 'l', 'l', 'l', 1, True, True, True, True)

    simple_3 = config.Config('simple-3', (50, 50), (6, 6), config.Tile.SOCKET)
    simple_3.add_tiles([p / 'blank.png'], 'blank', 'b', 'b', 'b', 'b', 1)
    # simple_3.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1)
    simple_3.add_tiles([p / 'line.png'], 'line', 'b', 'l', 'b', 'l', 1, True, True)
    simple_3.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'b', 'b', 1, True, True, True, True)
    # simple_3.add_tiles([p / 't.png'], 't', 'b', 'l', 'l', 'l', 1, True, True, True, True)

    simple_4 = config.Config('simple-4', (25, 25), (12, 12), config.Tile.SOCKET)
    simple_4.add_tiles([p / 'blank.png'], 'blank', 'b', 'b', 'b', 'b', 1)
    # simple_4.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 0.000001)
    # simple_4.add_tiles([p / 'line.png'], 'line', 'b', 'l', 'b', 'l', 1, True, True)
    # simple_4.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'b', 'b', 0.000001, True, True, True, True)
    simple_4.add_tiles([p / 't.png'], 't', 'b', 'l', 'l', 'l', 1, True, True, True, True)

    simple_5 = config.Config('simple-5', (50, 50), (6, 6), config.Tile.SOCKET)
    # simple_5.add_tiles([p / 'blank.png'], 'blank', 'b', 'b', 'b', 'b', 1)
    # simple_5.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1)
    # simple_5.add_tiles([p / 'line.png'], 'line', 'b', 'l', 'b', 'l', 1, True, True)
    # simple_5.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'b', 'b', 1, True, True, True, True)
    simple_5.add_tiles([p / 't.png'], 't', 'b', 'l', 'l', 'l', 1, True, True, True, True)

    simple_6 = config.Config('simple-6', (50, 50), (6, 6), config.Tile.SOCKET)
    # simple_6.add_tiles([p / 'blank.png'], 'blank', 'b', 'b', 'b', 'b', 1)
    # simple_6.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1)
    simple_6.add_tiles([p / 'line.png'], 'line', 'b', 'l', 'b', 'l', 1, True, True)
    simple_6.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'b', 'b', 1, True, True, True, True)
    # simple_6.add_tiles([p / 't.png'], 't', 'b', 'l', 'l', 'l', 1, True, True, True, True)

    simple_7 = config.Config('simple-7', (50, 50), (6, 6), config.Tile.SOCKET)
    simple_7.add_tiles([p / 'blank.png'], 'blank', 'b', 'b', 'b', 'b', 1)
    # simple_7.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1)
    # simple_7.add_tiles([p / 'line.png'], 'line', 'b', 'l', 'b', 'l', 1, True, True)
    simple_7.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'b', 'b', 1, True, True, True, True)
    # simple_7.add_tiles([p / 't.png'], 't', 'b', 'l', 'l', 'l', 1, True, True, True, True)

    simple_8 = config.Config('simple-8', (50, 50), (6, 6), config.Tile.SOCKET)
    # simple_8.add_tiles([p / 'blank.png'], 'blank', 'b', 'b', 'b', 'b', 1)
    # simple_8.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1)
    # simple_8.add_tiles([p / 'line.png'], 'line', 'b', 'l', 'b', 'l', 1, True, True)
    simple_8.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'b', 'b', 1, True, True, True, True)
    # simple_8.add_tiles([p / 't.png'], 't', 'b', 'l', 'l', 'l', 1, True, True, True, True)

    p = Path('samples/knots/')
    '''
    e - empty
    l - line
    '''
    knots_1 = config.Config('Knots Standard', (50, 50), conn_type=config.Tile.SOCKET)
    knots_1.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'e', 'e', 1, True, True, True, True)
    knots_1.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1, True, True)
    knots_1.add_tiles([p / 'empty.png'], 'empty', 'e', 'e', 'e', 'e', 1)
    knots_1.add_tiles([p / 'line.png'], 'line', 'e', 'l', 'e', 'l', 1, True, True)
    # knots_1.add_tiles([p / 't.png'], 't', 'e', 'l', 'l', 'l', 1, True, True, True, True)

    knots_2 = config.Config('Knots Dense', (50, 50), conn_type=config.Tile.SOCKET)
    knots_2.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'e', 'e', 1, True, True, True, True)
    knots_2.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1, True, True)
    # knots_2.add_tiles([p / 'empty.png'], 'empty', 'e', 'e', 'e', 'e', 1)
    knots_2.add_tiles([p / 'line.png'], 'line', 'e', 'l', 'e', 'l', 1, True, True)
    # knots_2.add_tiles([p / 't.png'], 't', 'e', 'l', 'l', 'l', 1, True, True, True, True)

    knots_3 = config.Config('Knots Crossless', (50, 50), conn_type=config.Tile.SOCKET)
    knots_3.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'e', 'e', 1, True, True, True, True)
    # knots_3.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1, True, True)
    knots_3.add_tiles([p / 'empty.png'], 'empty', 'e', 'e', 'e', 'e', 1)
    knots_3.add_tiles([p / 'line.png'], 'line', 'e', 'l', 'e', 'l', 1, True, True)
    # knots_3.add_tiles([p / 't.png'], 't', 'e', 'l', 'l', 'l', 1, True, True, True, True)

    knots_4 = config.Config('Knots TE', (25, 25), (20, 20), conn_type=config.Tile.SOCKET)
    # knots_4.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'e', 'e', 1, True, True, True, True)
    # knots_4.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1, True, True)
    knots_4.add_tiles([p / 'empty.png'], 'empty', 'e', 'e', 'e', 'e', 1)
    # knots_4.add_tiles([p / 'line.png'], 'line', 'e', 'l', 'e', 'l', 1, True, True)
    knots_4.add_tiles([p / 't.png'], 't', 'e', 'l', 'l', 'l', 1, True, True, True, True)

    knots_5 = config.Config('Knots T', (50, 50), conn_type=config.Tile.SOCKET)
    # knots_5.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'e', 'e', 1, True, True, True, True)
    # knots_5.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1, True, True)
    # knots_5.add_tiles([p / 'empty.png'], 'empty', 'e', 'e', 'e', 'e', 1)
    # knots_5.add_tiles([p / 'line.png'], 'line', 'e', 'l', 'e', 'l', 1, True, True)
    knots_5.add_tiles([p / 't.png'], 't', 'e', 'l', 'l', 'l', 1, True, True, True, True)

    knots_6 = config.Config('Knots CL', (50, 50), conn_type=config.Tile.SOCKET)
    knots_6.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'e', 'e', 1, True, True, True, True)
    # knots_6.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1, True, True)
    # knots_6.add_tiles([p / 'empty.png'], 'empty', 'e', 'e', 'e', 'e', 1)
    knots_6.add_tiles([p / 'line.png'], 'line', 'e', 'l', 'e', 'l', 1, True, True)
    # knots_6.add_tiles([p / 't.png'], 't', 'e', 'l', 'l', 'l', 1, True, True, True, True)

    knots_7 = config.Config('Knots CE', (50, 50), conn_type=config.Tile.SOCKET)
    knots_7.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'e', 'e', 1, True, True, True, True)
    # knots_7.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1, True, True)
    knots_7.add_tiles([p / 'empty.png'], 'empty', 'e', 'e', 'e', 'e', 1)
    # knots_7.add_tiles([p / 'line.png'], 'line', 'e', 'l', 'e', 'l', 1, True, True)
    # knots_7.add_tiles([p / 't.png'], 't', 'e', 'l', 'l', 'l', 1, True, True, True, True)

    knots_8 = config.Config('Knots C', (50, 50), conn_type=config.Tile.SOCKET)
    knots_8.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'e', 'e', 1, True, True, True, True)
    # knots_8.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1, True, True)
    # knots_8.add_tiles([p / 'empty.png'], 'empty', 'e', 'e', 'e', 'e', 1)
    # knots_8.add_tiles([p / 'line.png'], 'line', 'e', 'l', 'e', 'l', 1, True, True)
    # knots_8.add_tiles([p / 't.png'], 't', 'e', 'l', 'l', 'l', 1, True, True, True, True)

    knots_9 = config.Config('Knots Fabric', (50, 50), conn_type=config.Tile.SOCKET)
    # knots_9.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'e', 'e', 1, True, True, True, True)
    knots_9.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1, True, True)
    # knots_9.add_tiles([p / 'empty.png'], 'empty', 'e', 'e', 'e', 'e', 1)
    knots_9.add_tiles([p / 'line.png'], 'line', 'e', 'l', 'e', 'l', 1, True, True)
    # knots_9.add_tiles([p / 't.png'], 't', 'e', 'l', 'l', 'l', 1, True, True, True, True)

    knots_10 = config.Config('Knots Dense Fabric', (50, 50), conn_type=config.Tile.SOCKET)
    # knots_10.add_tiles([p / 'corner.png'], 'corner', 'l', 'l', 'e', 'e', 1, True, True, True, True)
    knots_10.add_tiles([p / 'cross.png'], 'cross', 'l', 'l', 'l', 'l', 1, True, True)
    # knots_10.add_tiles([p / 'empty.png'], 'empty', 'e', 'e', 'e', 'e', 1)
    # knots_10.add_tiles([p / 'line.png'], 'line', 'e', 'l', 'e', 'l', 1, True, True)
    # knots_10.add_tiles([p / 't.png'], 't', 'e', 'l', 'l', 'l', 1, True, True, True, True)

    x = 50
    p = Path('samples/circuit/')
    circuit = config.Config('Circuit', (x, x), conn_type=config.Tile.NAME)
    circuit.add_tiles([p / 'bridge.png'], 'bridge',
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_1', 'dskew_2', 'dskew_3', 'skew_0', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      ['wire_1', 'wire_3', 'bridge_1', 'bridge_3', 'transition_0'],
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_1', 'dskew_2', 'dskew_3', 'skew_0', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      ['wire_1', 'wire_3', 'bridge_1', 'bridge_3', 'transition_0'],
                      1, True, True)
    circuit.add_tiles([p / 'component.png'], 'component',
                      ['component_0', 'component_1', 'component_2', 'component_3', 'ecomponent_2', 'connection_2'],
                      ['component_0', 'component_1', 'component_2', 'component_3', 'ecomponent_2', 'connection_2'],
                      ['component_0', 'component_1', 'component_2', 'component_3', 'ecomponent_2', 'connection_2'],
                      ['component_0', 'component_1', 'component_2', 'component_3', 'ecomponent_2', 'connection_2'],
                      5)
    # circuit.add_tiles([p / 'ecomponent.png'], 'ecomponent',
    #                   ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
    #                   ['ecomponent_3', 'corner_3'],
    #                   ['component_0', 'component_1', 'component_2', 'component_3'],
    #                   ['ecomponent_1', 'corner_2'],
    #                   5, True, True, True, True)
    circuit.add_tiles([p / 'connection.png'], 'connection',
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_1', 'dskew_2', 'dskew_3', 'skew_0', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      ['connection_3', 'corner_3'],
                      ['component_0', 'component_1', 'component_2', 'component_3'],
                      ['connection_1', 'corner_2'],
                      10, True, True, True, True)
    circuit.add_tiles([p / 'corner.png'], 'corner',
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['connection_3', 'ecomponent_3'],
                      ['connection_1', 'ecomponent_1'],
                      10, True, True, True, True)
    circuit.add_tiles([p / 'dskew.png'], 'dskew',
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_2', 'skew_0', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_1', 'dskew_3', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_2', 'skew_0', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_1', 'dskew_3', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      2, True, True)
    circuit.add_tiles([p / 'skew.png'], 'skew',
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_2', 'skew_0', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_1', 'dskew_3', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      2, True, True, True, True)
    circuit.add_tiles([p / 'substrate.png'], 'substrate',
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      2)
    circuit.add_tiles([p / 't.png'], 't',
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_1', 'dskew_2', 'dskew_3', 'skew_0', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_1', 'dskew_2', 'dskew_3', 'skew_0', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_1', 'dskew_2', 'dskew_3', 'skew_0', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      0.1, True, True, True, True)
    circuit.add_tiles([p / 'track.png'], 'track',
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_1', 'dskew_2', 'dskew_3', 'skew_0', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_1', 'dskew_2', 'dskew_3', 'skew_0', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      2, True, True)
    circuit.add_tiles([p / 'transition.png'], 'transition',
                      ['wire_1', 'wire_3', 'bridge_1', 'bridge_3'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_1', 'dskew_2', 'dskew_3', 'skew_0', 'skew_1', 't_1', 't_2', 't_3', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      0.4, True, True, True, True)
    # circuit.add_tiles([p / 'turn.png'], 'turn',
    #                   ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_1', 'dskew_2', 'dskew_3', 'skew_0', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
    #                   ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_1', 'dskew_2', 'dskew_3', 'skew_0', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
    #                   ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
    #                   ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
    #                   1, True, True, True, True)
    circuit.add_tiles([p / 'viad.png'], 'viad',
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_1', 'dskew_2', 'dskew_3', 'skew_0', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_1', 'dskew_2', 'dskew_3', 'skew_0', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3', 'vias_0'],
                      0.1, True, True)
    circuit.add_tiles([p / 'vias.png'], 'vias',
                      ['track_0', 'track_2', 'connection_0', 'bridge_0', 'bridge_2', 'dskew_0', 'dskew_1', 'dskew_2', 'dskew_3', 'skew_0', 'skew_1', 't_1', 't_2', 't_3', 'transition_2', 'turn_0', 'turn_1', 'viad_1', 'viad_3'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      0.3, True, True, True, True)
    circuit.add_tiles([p / 'wire.png'], 'wire',
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['wire_1', 'wire_3', 'bridge_1', 'bridge_3', 'transition_0'],
                      ['substrate_0', 'substrate_1', 'substrate_2', 'substrate_3', 'ecomponent_0', 'corner_0', 'corner_1', 'skew_2', 'skew_3', 't_0', 'track_1', 'track_3', 'transition_1', 'transition_3', 'turn_2', 'turn_3', 'viad_0', 'viad_2', 'vias_1', 'vias_2', 'vias_3', 'wire_0', 'wire_2'],
                      ['wire_1', 'wire_3', 'bridge_1', 'bridge_3', 'transition_0'],
                      0.5, True, True)

    p = Path('samples/castle/')
    castle = config.Config('Castle', (25, 25), (14, 14), conn_type=config.Tile.NAME)
    castle.add_tiles([p / 'bridge.png'], 'bridge',
                     ['river_0', 'river_2', 'riverturn_0', 'riverturn_1', 'wallriver_1', 'wallriver_3'],
                     ['road_0', 'road_2', 'roadturn_0', 'roadturn_1', 't_1', 't_2', 't_3', 'wallroad_1', 'wallroad_3'],
                     ['river_0', 'river_2', 'riverturn_0', 'riverturn_1', 'wallriver_1', 'wallriver_3'],
                     ['road_0', 'road_2', 'roadturn_0', 'roadturn_1', 't_1', 't_2', 't_3', 'wallroad_1', 'wallroad_3'],
                     1,
                     True, True)
    castle.add_tiles([p / 'ground.png'], 'ground',
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'river_1', 'river_3', 'riverturn_2', 'riverturn_3', 'road_1', 'road_3', 'roadturn_2', 'roadturn_3', 't_0', 'wall_1', 'wall_3', 'tower_2', 'tower_3'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'river_1', 'river_3', 'riverturn_2', 'riverturn_3', 'road_1', 'road_3', 'roadturn_2', 'roadturn_3', 't_0', 'wall_1', 'wall_3', 'tower_2', 'tower_3'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'river_1', 'river_3', 'riverturn_2', 'riverturn_3', 'road_1', 'road_3', 'roadturn_2', 'roadturn_3', 't_0', 'wall_1', 'wall_3', 'tower_2', 'tower_3'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'river_1', 'river_3', 'riverturn_2', 'riverturn_3', 'road_1', 'road_3', 'roadturn_2', 'roadturn_3', 't_0', 'wall_1', 'wall_3', 'tower_2', 'tower_3'],
                     1)
    castle.add_tiles([p / 'river.png'], 'river',
                     ['river_0', 'river_2', 'riverturn_0', 'riverturn_1', 'bridge_0', 'bridge_2', 'wallriver_1', 'wallriver_3'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'road_1', 'road_3', 'roadturn_2', 'roadturn_3', 't_0', 'wall_1', 'wall_3', 'tower_2', 'tower_3'],
                     ['river_0', 'river_2', 'riverturn_0', 'riverturn_1', 'bridge_0', 'bridge_2', 'wallriver_1', 'wallriver_3'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'road_1', 'road_3', 'roadturn_2', 'roadturn_3', 't_0', 'wall_1', 'wall_3', 'tower_2', 'tower_3'],
                     1, True, True)
    castle.add_tiles([p / 'riverturn.png'], 'riverturn',
                     ['river_0', 'river_2', 'riverturn_0', 'bridge_0', 'bridge_2', 'wallriver_1', 'wallriver_3'],
                     ['river_0', 'river_2', 'riverturn_1', 'bridge_0', 'bridge_2', 'wallriver_1', 'wallriver_3'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'road_1', 'road_3', 'roadturn_2', 'roadturn_3', 't_0', 'wall_1', 'wall_3', 'tower_2', 'tower_3'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'road_1', 'road_3', 'roadturn_2', 'roadturn_3', 't_0', 'wall_1', 'wall_3', 'tower_2', 'tower_3'],
                     1, True, True, True, True)
    castle.add_tiles([p / 'road.png'], 'road',
                     ['road_0', 'road_2', 'roadturn_0', 'roadturn_1', 'bridge_1', 'bridge_3', 't_1', 't_2', 't_3', 'wallroad_1', 'wallroad_3'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'river_1', 'river_3', 'riverturn_2', 'riverturn_3', 'wall_1', 'wall_3', 'tower_2', 'tower_3'],
                     ['road_0', 'road_2', 'roadturn_0', 'roadturn_1', 'bridge_1', 'bridge_3', 't_1', 't_2', 't_3', 'wallroad_1', 'wallroad_3'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'river_1', 'river_3', 'riverturn_2', 'riverturn_3', 'wall_1', 'wall_3', 'tower_2', 'tower_3'],
                     1, True, True)
    castle.add_tiles([p / 'roadturn.png'], 'roadturn',
                     ['road_0', 'road_2', 'roadturn_0', 'bridge_1', 'bridge_3', 't_1', 'wallroad_1', 'wallroad_3'],
                     ['road_0', 'road_2', 'roadturn_1', 'bridge_1', 'bridge_3', 't_3', 'wallroad_1', 'wallroad_3'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'river_1', 'river_3', 'riverturn_2', 'riverturn_3', 'wall_1', 'wall_3', 'tower_2', 'tower_3'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'river_1', 'river_3', 'riverturn_2', 'riverturn_3', 'wall_1', 'wall_3', 'tower_2', 'tower_3'],
                     1, True, True, True, True)
    castle.add_tiles([p / 't.png'], 't',
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'river_1', 'river_3', 'riverturn_2', 'riverturn_3', 'wall_1', 'wall_3', 'tower_2', 'tower_3'],
                     ['road_0', 'road_2', 'roadturn_0', 'bridge_1', 'bridge_3', 't_1', 'wallroad_1', 'wallroad_3'],
                     ['road_0', 'road_2', 'bridge_1', 'bridge_3', 'wallroad_1', 'wallroad_3'],
                     ['road_0', 'road_2', 'roadturn_1', 'bridge_1', 'bridge_3', 't_3', 'wallroad_1', 'wallroad_3'],
                     1, True, True, True, True)
    castle.add_tiles([p / 'tower.png'], 'tower',
                     ['wall_0', 'wall_2', 'wallroad_0', 'wallroad_2', 'wallriver_0', 'wallriver_2'],
                     ['wall_0', 'wall_2', 'wallroad_0', 'wallroad_2', 'wallriver_0', 'wallriver_2'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'river_1', 'river_3', 'riverturn_2', 'riverturn_3', 'road_1', 'road_3', 'roadturn_2', 'roadturn_3', 't_0'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'river_1', 'river_3', 'riverturn_2', 'riverturn_3', 'road_1', 'road_3', 'roadturn_2', 'roadturn_3', 't_0'],
                     1, True, True, True, True)
    castle.add_tiles([p / 'wall.png'], 'wall',
                     ['wall_0', 'wall_2', 'tower_0', 'tower_1', 'wallroad_0', 'wallroad_2', 'wallriver_0', 'wallriver_2'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'river_1', 'river_3', 'riverturn_2', 'riverturn_3', 'road_1', 'road_3', 'roadturn_2', 'roadturn_3', 't_0'],
                     ['wall_0', 'wall_2', 'tower_0', 'tower_1', 'wallroad_0', 'wallroad_2', 'wallriver_0', 'wallriver_2'],
                     ['ground_0', 'ground_1', 'ground_2', 'ground_3', 'river_1', 'river_3', 'riverturn_2', 'riverturn_3', 'road_1', 'road_3', 'roadturn_2', 'roadturn_3', 't_0'],
                     1, True, True)
    castle.add_tiles([p / 'wallriver.png'], 'wallriver',
                     ['wall_0', 'wall_2', 'tower_0', 'tower_1', 'wallroad_0', 'wallroad_2'],
                     ['river_0', 'river_2', 'riverturn_0', 'riverturn_1', 'bridge_0', 'bridge_2'],
                     ['wall_0', 'wall_2', 'tower_0', 'tower_1', 'wallroad_0', 'wallroad_2'],
                     ['river_0', 'river_2', 'riverturn_0', 'riverturn_1', 'bridge_0', 'bridge_2'],
                     1,
                     True, True)
    castle.add_tiles([p / 'wallroad.png'], 'wallroad',
                     ['wall_0', 'wall_2', 'tower_0', 'tower_1', 'wallriver_0', 'wallriver_2'],
                     ['road_0', 'road_2', 'roadturn_0', 'roadturn_1', 'bridge_1', 'bridge_3', 't_1', 't_2', 't_3'],
                     ['wall_0', 'wall_2', 'tower_0', 'tower_1', 'wallriver_0', 'wallriver_2'],
                     ['road_0', 'road_2', 'roadturn_0', 'roadturn_1', 'bridge_1', 'bridge_3', 't_1', 't_2', 't_3'],
                     1, True, True)

    style = ttk.Style()
    # configure style: https://tkdocs.com/shipman/ttk-style-layer.html

    app = ui.App(
        simple_1, simple_2, simple_3, simple_4, simple_5, simple_6, simple_7, simple_8,
        knots_1, knots_2, knots_3, knots_4, knots_5, knots_6, knots_7, knots_8, knots_9, knots_10,
        castle,
        circuit,
    )

    app.mainloop()
