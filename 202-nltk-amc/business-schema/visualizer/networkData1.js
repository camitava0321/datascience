/**
 * 
 */
// create sample dataset
var sample_data = [
  {"name": "booked", "size": 10, "POS": "V"},
  {"name": "removed", "size": 10, "POS": "V"},
  {"name": "after", "size": 10, "POS": "V"},
  {"name": "rooms", "size": 30, "POS": "V"},
  {"name": "inventory", "size": 30, "POS": "V"}
]
// create list of node positions
var positions = [
  {"name": "booked", "x": 10, "y": 15},
  {"name": "removed", "x": 12, "y": 24},
  {"name": "after", "x": 16, "y": 18},
  {"name": "rooms", "x": 26, "y": 21},
  {"name": "inventory", "x": 13, "y": 4}
]
// create list of node connections
var connections = [
  {"source": "booked", "target": "removed", "strength": 1.25},
  {"source": "after", "target": "booked", "strength": 0.25},
  {"source": "rooms", "target": "booked", "strength": 2.25},
  {"source": "rooms", "target": "removed", "strength": 4.25},
  {"source": "inventory", "target": "removed", "strength": .85}
]

