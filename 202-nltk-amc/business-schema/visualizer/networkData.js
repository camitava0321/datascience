/**
 * 
 */
// create sample dataset
var sample_data = [
  {"name": "booked", "size": 10, "POS": "VBN"},
  {"name": "removed", "size": 10, "POS": "VBN"},
  {"name": "after", "size": 10, "POS": "IN"},
  {"name": "rooms", "size": 30, "POS": "NNS"},
  {"name": "inventory", "size": 30, "POS": "NN"}
]

// create list of node connections
var connections = [
  {"source": "booked", "target": "removed", "strength": 1, "UD": "advcl"},
  {"source": "after", "target": "booked", "strength": 1, "UD": "mark"},
  {"source": "rooms", "target": "booked", "strength": 1, "UD": "nsubj:pass"},
  {"source": "rooms", "target": "removed", "strength": 1, "UD": "nsubj:pass"},
  {"source": "inventory", "target": "removed", "strength": 1, "UD": "obl"}
]

 var attributes = [
    {"name": "rooms", "hex": "#CC0000"},
    {"name": "inventory", "hex": "#CC0000"},
    {"name": "booked", "hex": "#0000CC"},
    {"name": "removed", "hex": "#0000CC"},
    {"name": "after", "hex": "#004400"},
  ]