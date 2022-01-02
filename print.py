from transitions import Machine
from transitions.extensions import GraphMachine
from flask import Flask, jsonify, request, abort, send_file
#try:
import pygraphviz as pgv
#except ImportError:
#    raise
#import requests
machine = GraphMachine(
    states=["user", "state1", "state2","state3","state_lightroast"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state1",
            "conditions": "is_going_to_state1",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state2",
            "conditions": "is_going_to_state2",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state3",
            "conditions": "is_going_to_state3",
        },
        {
            "trigger": "advance",
            "source": "state1",
            "dest": "state_lightroast",
            "conditions": "is_going_to_state_lightroast",
        },
        {
            "trigger": "advance",
            "source": "state1",
            "dest": "state_mediumroast",
            "conditions": "is_going_to_state_mediumroast",
        },
        {
            "trigger": "advance",
            "source": "state1",
            "dest": "state3",
            "conditions": "is_going_to_state3",
        },
        {"trigger": "go_back", "source": ["state_lightroast","state_mediumroast","state2", "state3"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)
machine.get_graph().draw("finite_state_machine.png", prog="dot", format="png")